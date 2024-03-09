from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from animes import serializers as animes_serializers

from . import models

# Create your views here.


class ScheduleListItemSerializer(serializers.ModelSerializer):
    anime = animes_serializers.AnimeListItemSerializer(read_only=True)

    class Meta:
        model = models.Schedule
        fields = ("id", "anime", "episode", "date",)


class ScheduleAPIView(APIView):
    def get(self, request):
        schedules = models.Schedule.objects.all()
        serializer = ScheduleListItemSerializer(schedules, many=True)
        return Response(serializer.data)