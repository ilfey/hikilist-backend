from django.urls import path, include

from . import endpoints

urlpatterns = [
    path('', include(endpoints.router.urls)),
]