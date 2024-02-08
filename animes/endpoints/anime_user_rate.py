from rest_framework import serializers, viewsets, filters

from animes import models


class AnimeUserRateSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.AnimeUserRate
    fields = '__all__'


class AnimeUserRateViewSet(viewsets.ModelViewSet):
  queryset = models.AnimeUserRate.objects.all()
  serializer_class = AnimeUserRateSerializer
  filter_backends = [filters.SearchFilter]