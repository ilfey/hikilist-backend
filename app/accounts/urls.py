from django.urls import path

from accounts.views.auth import AuthViewSet

viewsets = [
    ("v1/auth", AuthViewSet, "auth"),
]

urlpatterns = []
