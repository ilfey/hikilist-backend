from rest_framework import serializers

from animes import models


class ListListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.List
        fields = "__all__"
