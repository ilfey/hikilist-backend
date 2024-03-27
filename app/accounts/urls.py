from django.urls import path

from accounts.views.auth import AuthViewSet
from accounts.views.accounts import AccountViewSet
from accounts.views.lists import ListViewSet
from accounts.views.rates import RateViewSet

viewsets = [
    ("v1/auth", AuthViewSet, "auth"),
    ("v1/accounts", AccountViewSet, "accounts"),
    ("v1/lists", ListViewSet, "lists"),
    ("v1/rates", RateViewSet, "rates"),
]

urlpatterns = []
