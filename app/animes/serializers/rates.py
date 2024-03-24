from rest_framework import serializers

from accounts.serializers.users import UserListSerializer

from animes import models

from .animes import AnimeListSerializer


class RateListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    anime = AnimeListSerializer(read_only=True)

    class Meta:
        model = models.AnimeUserRate
        fields = (
            "id",
            "user",
            "anime",
            "list",
            "rating",
        )
        read_only_fields = (
            "id",
            "user",
        )
        depth = 1
