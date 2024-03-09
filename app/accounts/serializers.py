from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username"]
        read_only_fields = ["id", "username"]


class AuthenticateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=3, max_length=32)
    password = serializers.CharField(required=True, min_length=6, max_length=32)
