from rest_framework import serializers

from animes import models


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = "__all__"
