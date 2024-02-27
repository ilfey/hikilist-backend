from django.urls import path, include

from animes import views

from . import endpoints

urlpatterns = [
    path('', include(endpoints.router.urls)),
    # path('accounts/anime_user_rates/', views.UserListView.as_view(), name="user-list")
]