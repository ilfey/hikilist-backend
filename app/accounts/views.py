import json

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
from django.views.decorators.http import require_POST


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from animes.endpoints.anime_user_rate import AnimeUserRateSerializer
from animes import models as animes_models

from . import models

from . import serializers

# Create your views here.


def get_csrf(request):
    response = JsonResponse({"detail": "CSRF cookie set"})
    response["X-CSRFToken"] = get_token(request)
    return response


@require_POST
@requires_csrf_token
def login_view(request):
    data = serializers.AuthenticateSerializer(data=json.loads(request.body))

    if not data.is_valid():
        return JsonResponse(
            {
                "errors": data.errors,
                "detail": "Invalid body.",
            },
            status=400,
        )

    user = authenticate(username=data["username"].value, password=data["password"].value)

    if user is None:
        return JsonResponse({"detail": "Invalid credentials."}, status=400)

    login(request, user)
    return JsonResponse({"detail": "Successfully logged in."})


@require_POST
@requires_csrf_token
def register_view(request):
    data = serializers.AuthenticateSerializer(data=json.loads(request.body))

    if not data.is_valid():
        return JsonResponse(
            {
                "errors": data.errors,
                "detail": "Invalid body.",
            },
            status=400,
        )

    username = data["username"].value
    password = data["password"].value

    if models.User.objects.filter(username=username).exists():
        return JsonResponse({"detail": "Username already exists."}, status=409)

    user = models.User.objects.create_user(
        username=username,
        password=password,
    )

    return JsonResponse(
        {
            "id": user.id,
            "username": user.username,
            "detail": "Successfully registered.",
        }
    )


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "You're not logged in."}, status=400)

    logout(request)

    return JsonResponse({"detail": "Successfully logged out."})


# @ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})

    return JsonResponse({"isAuthenticated": True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False}, status=401)

    return JsonResponse(
        {
            "id": request.user.id,
            "username": request.user.username,
        }
    )


class UserListView(APIView):
    def get(self, request, user_id, list_id):
        if user_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if list_id == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = animes_models.AnimeUserRate.objects.filter(list=list_id)
        serializer = AnimeUserRateSerializer(data, many=True)

        return Response(serializer.data)
