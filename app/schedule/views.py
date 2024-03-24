from rest_framework import viewsets, filters

from .serializers import ScheduleListSerializer

from . import models


class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = ScheduleListSerializer
    filter_backends = (filters.OrderingFilter,)
