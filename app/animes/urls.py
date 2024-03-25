from django.urls import path, include

from animes.views.animes import AnimeViewSet
from animes.views.formats import FormatViewSet
from animes.views.genres import GenreViewSet
from animes.views.lists import ListViewSet
from animes.views.rates import RateViewSet
from animes.views.studios import StudioViewSet

viewsets = [
    ("v1/animes", AnimeViewSet, "animes"),
    ("v1/formats", FormatViewSet, "formats"),
    ("v1/genres", GenreViewSet, "genres"),
    ("v1/lists", ListViewSet, "lists"),
    ("v1/rates", RateViewSet, "rates"),
    ("v1/studios", StudioViewSet, "studios"),
]

urlpatterns = []
