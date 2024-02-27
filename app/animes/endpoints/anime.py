from rest_framework import serializers, viewsets, filters

from animes import models


class AnimeListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anime
        fields = ["id", "title", "poster", "episodes", "episodes_released", "genres", "studios", "format",]
        depth = 1


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anime
        fields = "__all__"
        depth = 1


class AnimeViewSet(viewsets.ModelViewSet):
	queryset = models.Anime.objects.all()
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ("id", "title", "description",)

	def get_serializer_class(self):
		if hasattr(self, "action") and self.action == 'list':
			return AnimeListItemSerializer
	
		return AnimeSerializer