from django.urls import path

from . import views

viewsets = [
    ("schedule", views.ScheduleViewSet, "schedule"),
]

urlpatterns = []
