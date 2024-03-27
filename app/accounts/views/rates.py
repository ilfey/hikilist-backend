from django.db import IntegrityError

from rest_framework import viewsets, mixins, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.serializers.rates import RateListSerializer, RateSerializer

from accounts import models


class RateViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Rate.objects.all()
    serializer_class = RateListSerializer
    filter_backends = (filters.OrderingFilter,)
    lookup_url_kwarg = "rate_pk"

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]

        return super().get_permissions()

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return RateSerializer

        return super().get_serializer_class(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {
                    "detail": "Rate already exists.",
                },
                status=status.HTTP_409_CONFLICT,
            )
