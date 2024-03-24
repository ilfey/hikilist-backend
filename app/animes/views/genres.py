from rest_framework import viewsets, filters

from animes import models

from animes.serializers.genres import GenreListSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = GenreListSerializer
    filter_backends = (filters.OrderingFilter,)
