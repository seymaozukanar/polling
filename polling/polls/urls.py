from django.urls import path
from .views import PollCreateView, PollListView, VoteCreateView


urlpatterns = [
    path("", PollListView.as_view(), name="poll-list"),
    path("create/", PollCreateView.as_view(), name="poll-create"),
    path("vote/", VoteCreateView.as_view(), name="vote")
]
