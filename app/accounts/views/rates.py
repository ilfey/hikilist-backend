from drf_spectacular.utils import extend_schema, extend_schema_view

from django.db import IntegrityError

from django_filters import rest_framework as dj_filters

from rest_framework import viewsets, mixins, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.serializers.rates import RateListSerializer, RateSerializer

from accounts import models


@extend_schema_view(
    list=extend_schema(
        summary="Get rates",
    ),
    retrieve=extend_schema(
        summary="Get details of rate",
    ),
    create=extend_schema(
        summary="Create new rate",
    ),
    update=extend_schema(
        summary="Update rate",
    ),
    partial_update=extend_schema(
        summary="Partial update rate",
    ),
    destroy=extend_schema(
        summary="Delete rate",
    ),
)
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
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    lookup_url_kwarg = "rate_pk"
    filterset_fields = {
        "user__id": ("exact",),
        "anime__id": ("exact",),
        "rating": (
            "gt",
            "lt",
        ),
        "list__id": ("exact",),
    }

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
        except IntegrityError as e:
            print(e)
            return Response(
                {
                    "detail": "Rate already exists.",
                },
                status=status.HTTP_409_CONFLICT,
            )
