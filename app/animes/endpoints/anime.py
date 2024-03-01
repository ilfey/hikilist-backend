from rest_framework import serializers, viewsets, filters, pagination

from animes import models


class AnimeListItemSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = models.Anime
        fields = ["id", "title", "poster", "episodes", "episodes_released", "genres", "studios", "format",]
        depth = 1
    
    def get_poster(self, anime):
        if str(anime.poster).startswith("http"):
            return str(anime.poster)

        return str(anime.poster.url)


class AnimeSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    related = AnimeListItemSerializer(many=True)

    class Meta:
        model = models.Anime
        fields = "__all__"
        depth = 1
    
    def get_poster(self, anime):
        if str(anime.poster).startswith("http"):
            return str(anime.poster)

        return str(anime.poster.url)


class AnimePagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100000


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = models.Anime.objects.all()
    pagination_class = AnimePagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ("id", "title", "description",)

    def get_serializer_class(self):
        if hasattr(self, "action") and self.action == 'list':
            return AnimeListItemSerializer
    
        return AnimeSerializer