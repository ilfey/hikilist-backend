from helpers.serializers import CurrentUserIdDefault

from rest_framework import serializers

from animes.serializers.animes import AnimeListSerializer

from accounts import models

from .accounts import AccountListSerializer
from .lists import ListListSerializer

from animes.models import Anime


class RateListSerializer(serializers.ModelSerializer):
    user = AccountListSerializer(read_only=True)
    anime = AnimeListSerializer(read_only=True)
    list = ListListSerializer(read_only=True)

    class Meta:
        model = models.Rate
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


class RateSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=CurrentUserIdDefault())
    user = AccountListSerializer(read_only=True)

    anime_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Anime.objects.all(), required=True
    )
    anime = AnimeListSerializer(read_only=True)

    list_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=models.List.objects.all(), required=True
    )
    list = ListListSerializer(read_only=True)

    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = models.Rate
        fields = "__all__"
