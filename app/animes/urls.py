from django.urls import path, include

from animes.views.animes import AnimeViewSet
from animes.views.formats import FormatViewSet
from animes.views.genres import GenreViewSet
from animes.views.lists import ListViewSet
from animes.views.rates import RateViewSet
from animes.views.studios import StudioViewSet

viewsets = [
    ("animes", AnimeViewSet, "animes"),
    ("formats", FormatViewSet, "formats"),
    ("genres", GenreViewSet, "genres"),
    ("lists", ListViewSet, "lists"),
    ("rates", RateViewSet, "rates"),
    ("studios", StudioViewSet, "studios"),
]

urlpatterns = []
