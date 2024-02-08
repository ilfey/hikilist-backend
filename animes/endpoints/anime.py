from rest_framework import serializers, viewsets, filters

from animes import models


class AnimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Anime
    fields = '__all__'


class AnimeViewSet(viewsets.ModelViewSet):
  queryset = models.Anime.objects.all()
  serializer_class = AnimeSerializer
  filter_backends = [filters.SearchFilter]