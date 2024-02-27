
from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/<int:user_id>/lists/', views.UserListsStats.as_view(), name="stats-user-lists")
]