from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, filters

from animes import models

from animes.serializers.formats import FormatListSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get formats",
    ),
    retrieve=extend_schema(
        summary="Get details of format",
    ),
)
class FormatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Format.objects.all()
    serializer_class = FormatListSerializer
    filter_backends = (filters.OrderingFilter,)
