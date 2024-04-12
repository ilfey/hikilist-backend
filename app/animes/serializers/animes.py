from rest_framework import serializers

from animes import models
from .studios import StudioListSerializer
from .genres import GenreListSerializer
from .formats import FormatListSerializer


class AnimeListSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    genres = GenreListSerializer(many=True, read_only=True)
    studios = StudioListSerializer(many=True, read_only=True)
    format = FormatListSerializer(read_only=True)

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

    def get_poster(self, anime):
        if anime.poster == "":
            return None

        if str(anime.poster).startswith("http"):
            return str(anime.poster)

        return str(anime.poster.url)


class AnimeSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    related = AnimeListSerializer(many=True)
    genres = GenreListSerializer(many=True)
    studios = StudioListSerializer(many=True)
    format = FormatListSerializer()

    def get_poster(self, anime):
        if anime.poster == "":
            return None

        if str(anime.poster).startswith("http"):
            return str(anime.poster)

        return str(anime.poster.url)

    class Meta:
        model = models.Anime
        fields = "__all__"
