from rest_framework import serializers

from animes import models


class StudioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Studio
        fields = "__all__"
