from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, filters

from animes import models

from animes.serializers.studios import StudioListSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get studios",
    ),
    retrieve=extend_schema(
        summary="Get details of studio",
    ),
)
class StudioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = StudioListSerializer
    filter_backends = (filters.OrderingFilter,)
