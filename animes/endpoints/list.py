from rest_framework import serializers, viewsets, filters

from animes import models


class ListSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.List
    fields = '__all__'


class ListViewSet(viewsets.ModelViewSet):
  queryset = models.List.objects.all()
  serializer_class = ListSerializer
  filter_backends = [filters.SearchFilter]