from django.urls import path
from .views import list_polls

urlpatterns = [
    path("", list_polls, name="list_polls"),
]
