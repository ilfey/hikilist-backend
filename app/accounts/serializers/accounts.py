from rest_framework import serializers

from accounts import models


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "id",
            "username",
        )
