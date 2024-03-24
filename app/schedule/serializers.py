from rest_framework import serializers

from animes.serializers.animes import AnimeListSerializer

from . import models


class ScheduleListSerializer(serializers.ModelSerializer):
    anime = AnimeListSerializer(read_only=True)

    class Meta:
        model = models.Schedule
        fields = (
            "id",
            "anime",
            "episode",
            "date",
        )
