import json

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
from django.views.decorators.http import require_POST

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from animes.endpoints.anime_user_rate import AnimeUserRateSerializer
from animes import models as animes_models

from . import models

from . import serializers

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        serializer = serializers.AuthenticateSerializer(data=request.data)

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
            return Response({
                "detail": "Invalid credentials."
            }, status=status.HTTP_401_UNAUTHORIZED)

        # Create refresh token
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        })


class RegisterView(APIView):
    def post(self, request):
        serializer = serializers.AuthenticateSerializer(data=request.data)
        
        # Validate body
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # If user already exists then return conflict
        if models.User.objects.filter(username=serializer["username"].value).exists():
            return Response({
                "detail": "Username already exists."
            }, status=status.HTTP_409_CONFLICT)

        # Save user
        user = serializer.save()

        # Create refresh token
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    def post(self, request):
        serializer = TokenRefreshSerializer(data=request.data)

        try:
            # If body not valid then send bad request
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as ex:
            return Response({
                "detail": str(ex)
            }, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(serializer["refresh"].value)

        # add token to blacklist
        token.blacklist()
            
        return Response({
            "detail": "Successfully logged out."
        })


class UserListView(APIView):
    def get(self, request, user_id, list_id):
        #  If user_id is None then send bad request
        if not user_id:
            return Response({
                "detail": "Param user_id is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        # If list_id is None then send bad request
        if not list_id:
            return Response({
                "detail": "Param list_id is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        # Filter AnimesUserRate by list and serialize it.
        data = animes_models.AnimeUserRate.objects.filter(list=list_id)        
        serializer = AnimeUserRateSerializer(data, many=True)

        return Response(serializer.data)
