from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, filters

from .serializers import ScheduleListSerializer

from . import models


@extend_schema_view(
    list=extend_schema(
        summary="Get schedule (experimental)",
    ),
    retrieve=extend_schema(
        summary="Get details schedule (experimental)",
    ),
)
class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = ScheduleListSerializer
    filter_backends = (filters.OrderingFilter,)
