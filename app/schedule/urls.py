from django.urls import path

from . import views

urlpatterns = [
    path('', views.ScheduleAPIView.as_view(), name="schedule"),
]