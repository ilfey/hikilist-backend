from django.urls import path

from accounts.views.auth import AuthViewSet

viewsets = [
    ("auth", AuthViewSet, "auth"),
]

urlpatterns = []
