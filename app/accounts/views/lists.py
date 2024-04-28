from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, mixins

from accounts import models

from accounts.serializers.lists import ListListSerializer, ListSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get lists",
    ),
    retrieve=extend_schema(
        summary="Get details of lists",
    ),
    create=extend_schema(
        summary="Create new list",
    ),
    update=extend_schema(
        summary="Update list",
    ),
    partial_update=extend_schema(
        summary="Partial update list",
    ),
    destroy=extend_schema(
        summary="Delete list",
    ),
)
class ListViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.List.objects.all()
    serializer_class = ListListSerializer
    filter_backends = (filters.OrderingFilter,)
    lookup_url_kwarg = "list_pk"

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]

        return super().get_permissions()

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ListSerializer

        return super().get_serializer_class(*args, **kwargs)
