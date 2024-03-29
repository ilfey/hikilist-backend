from rest_framework import serializers

from accounts import models


class AuthenticateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=3, max_length=32)
    password = serializers.CharField(required=True, min_length=6, max_length=32)

    def save(self):
        return models.User.objects.create_user(
            username=self["username"].value,
            password=self["password"].value,
        )
