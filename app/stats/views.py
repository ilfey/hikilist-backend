from django.shortcuts import render
from django.db.models import Count, Avg, Q, OuterRef, Subquery
from django.db.models.functions import Coalesce

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

from animes import models as animes_models
from accounts import models as accounts_models
from accounts.serializers.user import UserListSerializer


class ListStatsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    count = serializers.IntegerField(read_only=True)


class CommonStatsSerializer(serializers.Serializer):
    count = serializers.IntegerField(read_only=True)
    rates_count = serializers.IntegerField(read_only=True)
    rates_avg = serializers.FloatField(read_only=True)


class UserListsStatsSerializer(serializers.Serializer):
    account = UserListSerializer(read_only=True)
    lists = ListStatsSerializer(many=True, read_only=True)
    total = serializers.IntegerField(read_only=True)
    common = CommonStatsSerializer(read_only=True)


class UserListsStats(APIView):
    def get(self, request, user_id):
        
        user = accounts_models.User.objects.get(id=user_id)

        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        sub = animes_models.AnimeUserRate.objects.filter(user=user_id, list_id=OuterRef("pk")).values("pk").annotate(count = Count("pk", distinct=True))

        lists_stats = animes_models.List.objects.annotate(count = Coalesce(Subquery(sub.values("count")), 0))

        # lists_stats = animes_models.AnimeUserRate.objects.filter(user=user_id)\
        #     .values("list__id", "list__title").annotate(count = Count("anime"))

        common_stats = animes_models.AnimeUserRate.objects.filter(user=user_id)\
            .aggregate(
                count = Count("id"),
                rates_count = Count("rating", filter=Q(rating__gt=0)),
                rates_avg = Avg("rating", filter=Q(rating__gt=0), default=0),
            )

        user_lists_stats_data = UserListsStatsSerializer({
            "account": user,
            "lists": lists_stats,
            "common": common_stats,
        })

        return Response(user_lists_stats_data.data)