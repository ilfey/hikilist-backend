from rest_framework import viewsets, filters

from animes.serializers.rates import RateListSerializer
from animes import models


class RateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RateListSerializer
    queryset = models.Rate.objects.all()
    filter_backends = (filters.OrderingFilter,)
