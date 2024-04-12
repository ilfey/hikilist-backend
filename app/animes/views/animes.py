from django_filters import rest_framework as dj_filters

from rest_framework import viewsets, pagination, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from animes.serializers.animes import AnimeSerializer, AnimeListSerializer
from animes import models

from accounts.models import Rate
from accounts.serializers.rates import RateSerializer

class AnimePagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 100000


class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AnimeListSerializer
    queryset = models.Anime.objects.all()
    pagination_class = AnimePagination
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    lookup_url_kwarg = "anime_pk"
    search_fields = (
        "id",
        "title",
        "description",
    )
    filterset_fields = {
        "episodes": (
            "gt",
            "lt",
        ),
        "episodes_released": (
            "gt",
            "lt",
        ),
        "announcement": (
            "year__gt",
            "year__lt",
        ),
        "started": (
            "year__gt",
            "year__lt",
        ),
        "released": (
            "year__gt",
            "year__lt",
        ),
        "genres__id": ("in",),
        "format__id": ("in",),
        "studios__id": ("in",),
    }

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "retrieve":
            return AnimeSerializer

        return super().get_serializer_class(*args, **kwargs)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy", "rate_detail"]:
            return [IsAuthenticated()]

        return super().get_permissions()

    @action(methods=["GET"], detail=True, url_path="rate")
    def rate_detail(self, request, anime_pk):
        if not Rate.objects.filter(user=request.user, anime_id=anime_pk).exists():
            return Response({"detail": "Rate not found"}, status=404)

        data = Rate.objects.filter(user=request.user, anime_id=anime_pk).get()
        serializer = RateSerializer(data)

        return Response(serializer.data)
