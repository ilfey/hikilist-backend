from rest_framework import viewsets, filters

from animes import models

from animes.serializers.lists import ListListSerializer


class ListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.List.objects.all()
    serializer_class = ListListSerializer
    filter_backends = (filters.OrderingFilter,)
