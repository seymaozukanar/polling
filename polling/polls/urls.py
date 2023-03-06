from django.urls import path
from .views import list_polls, poll_detail

urlpatterns = [
    path("", list_polls, name="list_polls"),
    path("<int:id>/", poll_detail, name="poll_detail")
]
