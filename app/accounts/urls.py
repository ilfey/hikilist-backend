from django.urls import path
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="api-login"),
    path("register/", views.RegisterView.as_view(), name="api-register"),
    path("refresh/", TokenRefreshView.as_view(), name="api-refresh"),
    path("logout/", views.LogoutView.as_view(), name="api-logout"),
    path(
        "<int:user_id>/list/<int:list_id>/",
        views.UserListView.as_view(),
        name="user-list",
    ),
]
