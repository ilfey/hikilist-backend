from django.urls import path

from . import views

viewsets = [
    ("v1/schedule", views.ScheduleViewSet, "schedule"),
]

urlpatterns = []
