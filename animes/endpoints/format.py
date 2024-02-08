from rest_framework import serializers, viewsets, filters

from animes import models


class FormatSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Format
    fields = '__all__'


class FormatViewSet(viewsets.ModelViewSet):
  queryset = models.Format.objects.all()
  serializer_class = FormatSerializer
  filter_backends = [filters.SearchFilter]