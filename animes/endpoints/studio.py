from rest_framework import serializers, viewsets, filters

from animes import models


class StudioSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Studio
    fields = '__all__'


class StudioViewSet(viewsets.ModelViewSet):
  queryset = models.Studio.objects.all()
  serializer_class = StudioSerializer
  filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
  search_fields = ("id", "title",)