from rest_framework import routers

from . import anime_user_rate, anime, format, genre, list, studio

router = routers.SimpleRouter()

router.register('anime_user_rates', anime_user_rate.AnimeUserRateViewSet)
router.register('animes', anime.AnimeViewSet)
router.register('formats', format.FormatViewSet)
router.register('genres', genre.GenreViewSet)
router.register('lists', list.ListViewSet)
router.register('studios', studio.StudioViewSet)