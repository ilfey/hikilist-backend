from rest_framework import serializers

from animes import models


class FormatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Format
        fields = "__all__"
