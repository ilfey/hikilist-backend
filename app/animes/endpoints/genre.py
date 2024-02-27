from rest_framework import serializers, viewsets, filters

from animes import models


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Genre
		fields = '__all__'


class GenreViewSet(viewsets.ModelViewSet):
	queryset = models.Genre.objects.all()
	serializer_class = GenreSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ("id", "title",)