from rest_framework import viewsets, filters

from animes import models

from animes.serializers.formats import FormatListSerializer


class FormatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Format.objects.all()
    serializer_class = FormatListSerializer
    filter_backends = (filters.OrderingFilter,)
