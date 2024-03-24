from rest_framework import serializers

from accounts import models


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "id",
            "username",
        )
