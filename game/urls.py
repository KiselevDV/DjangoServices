from django.urls import path

from .views import GameAPI

urlpatterns = [
    path('', GameAPI.as_view())
]
