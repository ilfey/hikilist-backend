from rest_framework import serializers, viewsets, filters

from animes import models
from accounts.serializers.user import UserListSerializer

from .anime import AnimeListItemSerializer


class AnimeUserRateSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    anime = AnimeListItemSerializer(read_only=True)

    class Meta:
        model = models.AnimeUserRate
        fields = [
            "id",
            "user",
            "anime",
            "list",
            "rating",
        ]
        read_only_fields = [
            "id",
            "user",
        ]
        depth = 1


class AnimeUserRateViewSet(viewsets.ModelViewSet):
    queryset = models.AnimeUserRate.objects.all()
    serializer_class = AnimeUserRateSerializer
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    # search_fields = ()
