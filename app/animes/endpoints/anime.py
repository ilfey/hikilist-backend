from rest_framework import serializers, viewsets, filters, pagination
from django_filters import rest_framework as dj_filters 

from animes import models


class AnimeListItemSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = models.Anime
        fields = ("id", "title", "poster", "episodes", "episodes_released", "status", "genres", "studios", "format",)
        depth = 1
    
    def get_poster(self, anime):
        if str(anime.poster).startswith("http"):
            return str(anime.poster)

        return str(anime.poster.url)


class AnimeSerializer(serializers.ModelSerializer):
    related = AnimeListItemSerializer(many=True)

    class Meta:
        model = models.Anime
        fields = "__all__"
        depth = 1


class AnimePagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100000


class AnimeFilter(dj_filters.FilterSet):
    class Meta:
        model = models.Anime
        fields = {
            "episodes": ("gt", "lt",),
            "episodes_released": ("gt", "lt",),
            
            "announcement": ("year__gt", "year__lt",),
            "started": ("year__gt", "year__lt",),
            "released": ("year__gt", "year__lt",),

            "genres": ("in",),
            "format": ("in",),
            "studios": ("in",),
        }


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = models.Anime.objects.all()
    pagination_class = AnimePagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = AnimeFilter
    search_fields = ("id", "title", "description",)

    def get_serializer_class(self):
        if hasattr(self, "action") and self.action == 'list':
            return AnimeListItemSerializer
    
        return AnimeSerializer