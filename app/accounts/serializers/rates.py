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
            "rewatched",
            "completed",
        )
        read_only_fields = (
            "id",
            "user",
        )


class RateSerializer(serializers.ModelSerializer):
    user = AccountListSerializer(read_only=True)

    anime_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Anime.objects.all(),
        required=True,
    )
    anime = AnimeListSerializer(read_only=True)

    list_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=models.List.objects.all(),
        required=True,
    )
    list = ListListSerializer(read_only=True)

    rating = serializers.IntegerField(
        required=False,
        allow_null=True,
        min_value=1,
        max_value=5,
        default=None,
    )

    completed = serializers.IntegerField(
        required=False,
        default=0,
    )

    def create(self, validated_data):
        data = validated_data.copy()

        data["user"] = self.context["request"].user

        data["anime"] = data.pop("anime_id")
        data["list"] = data.pop("list_id")

        return super().create(data)

    def update(self, instance, validated_data):
        data = validated_data.copy()

        data["list"] = data.pop("list_id")

        return super().update(instance, data)

    def validate(self, attrs):
        if self.instance:  # If instance is not None (update method)
            completed = attrs.get("completed")

            # If completed is not None, check if anime have enough episodes
            if completed and self.instance.anime.episodes_released < completed:

                raise serializers.ValidationError(
                    {"completed": "Not enough episodes released"}
                )

        elif (
            "completed" in attrs and "anime_id" in attrs
        ):  # If completed and anime_id in attrs (create method)
            anime = attrs.get("anime_id")
            complited = attrs.get("completed", 0)

            # Check if anime have enough episodes
            if anime.episodes_released < complited:

                raise serializers.ValidationError(
                    {"completed": "Not enough episodes released"}
                )

        return super().validate(attrs)

    class Meta:
        model = models.Rate
        fields = "__all__"
