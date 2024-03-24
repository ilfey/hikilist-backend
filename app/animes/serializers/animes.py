from rest_framework import serializers

from animes import models


class AnimeListSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = models.Anime
        fields = (
            "id",
            "title",
            "poster",
            "episodes",
            "episodes_released",
            "status",
            "genres",
            "studios",
            "format",
        )
        depth = 1

    def get_poster(self, anime):
        if str(anime.poster).startswith("http"):
            return str(anime.poster)

        return str(anime.poster.url)


class AnimeSerializer(serializers.ModelSerializer):
    related = AnimeListSerializer(many=True)

    class Meta:
        model = models.Anime
        fields = "__all__"
        depth = 1
