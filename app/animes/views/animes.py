from django_filters import rest_framework as dj_filters

from rest_framework import viewsets, pagination, filters

from animes.serializers.animes import AnimeSerializer, AnimeListSerializer
from animes import models


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

    def get_serializer(self, *args, **kwargs):
        if self.action == "retrieve":
            return AnimeSerializer

        return super().get_serializer(*args, **kwargs)
