from rest_framework import serializers

from animes.serializers.animes import AnimeListSerializer

from accounts import models

from .accounts import AccountListSerializer

from animes.models import Anime


class RateListSerializer(serializers.ModelSerializer):
    user = AccountListSerializer(read_only=True)
    anime = AnimeListSerializer(read_only=True)

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
        depth = 1


class RateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=models.User.objects.all(), default=serializers.CurrentUserDefault()
    )
    anime = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all())
    list = serializers.PrimaryKeyRelatedField(queryset=models.List.objects.all(), required=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = models.Rate
        fields = "__all__"
        depth = 1
