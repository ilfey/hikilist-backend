from django.contrib.auth import authenticate

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer,
    TokenObtainPairSerializer,
)
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import TokenError

from accounts.serializers.auth import AuthenticateSerializer

from accounts import models


@extend_schema_view(
    login=extend_schema(
        summary="Login into the account",
        responses={
            200: TokenObtainPairSerializer,
        },
    ),
    register=extend_schema(
        summary="Register a new account",
        responses={
            200: TokenObtainPairSerializer,
        },
    ),
    logout=extend_schema(
        summary="Logout from the account",
        request=TokenRefreshSerializer,
        responses={
            200: None
        }
    ),
    refresh=extend_schema(
        summary="Refresh access token",
        request=TokenRefreshSerializer,
        responses={
            200: TokenRefreshSerializer,
        },
    ),
)
class AuthViewSet(viewsets.GenericViewSet):

    serializer_class = AuthenticateSerializer

    @action(methods=["POST"], detail=False)
    def login(self, request):
        serializer = AuthenticateSerializer(data=request.data)

        # Validate body
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get user
        user = authenticate(
            username=serializer["username"].value,
            password=serializer["password"].value,
        )

        # If user is None then send bad request
        if not user:
            return Response(
                {"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
            )

        # Create refresh token
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = AuthenticateSerializer(data=request.data)

        # Validate body
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If user already exists then return conflict
        if models.User.objects.filter(username=serializer["username"].value).exists():
            return Response(
                {
                    "detail": "Username already exists.",
                },
                status=status.HTTP_409_CONFLICT,
            )

        # Save user
        user = serializer.save()

        # Create refresh token
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )

    @action(methods=["POST"], detail=False)
    def logout(self, request):
        serializer = TokenRefreshSerializer(data=request.data)

        try:
            # If body not valid then send bad request
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as ex:
            return Response({"detail": str(ex)}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(serializer["refresh"].value)

        # add token to blacklist
        token.blacklist()

        return Response({"detail": "Successfully logged out."})

    @action(methods=["POST"], detail=False)
    def refresh(self, request):
        return TokenRefreshView.as_view()(request)
