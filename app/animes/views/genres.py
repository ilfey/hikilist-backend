from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, filters

from animes import models

from animes.serializers.genres import GenreListSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get genres",
    ),
    retrieve=extend_schema(
        summary="Get details of genre",
    ),
)
class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = GenreListSerializer
    filter_backends = (filters.OrderingFilter,)
