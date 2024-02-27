from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('csrf/', views.get_csrf, name='api-csrf'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
    path('session/', views.session_view, name='api-session'),
    path('whoami/', views.whoami_view, name='api-whoami'),
    path('<int:user_id>/list/<int:list_id>/', views.UserListView.as_view(), name="user-list"),
]