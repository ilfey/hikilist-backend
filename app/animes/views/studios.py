from rest_framework import viewsets, filters

from animes import models

from animes.serializers.studios import StudioListSerializer


class StudioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = StudioListSerializer
    filter_backends = (filters.OrderingFilter,)
