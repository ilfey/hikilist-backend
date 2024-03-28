from helpers.serializers import CurrentUserIdDefault

from rest_framework import serializers

from accounts import models

from accounts.serializers.accounts import AccountListSerializer


class ListListSerializer(serializers.ModelSerializer):
    user = AccountListSerializer(read_only=True)

    class Meta:
        model = models.List
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=3, max_length=256)

    user_id = serializers.HiddenField(default=CurrentUserIdDefault())
    user = AccountListSerializer(read_only=True)

    is_primary = serializers.ReadOnlyField(default=False)

    class Meta:
        model = models.List
        fields = "__all__"
