from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username"]
        read_only_fields = ["id", "username"]


class ClaimsSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["user_id"] = user.id
        token["username"] = user.username

        return token


class AuthenticateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=3, max_length=32)
    password = serializers.CharField(required=True, min_length=6, max_length=32)

    def save(self):
        return models.User.objects.create_user(
            username=self["username"].value,
            password=self["password"].value,
        )