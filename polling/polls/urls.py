from django.urls import path
from .views import PollCreateView, PollListView, PollDetailView, VoteCreateView


urlpatterns = [
    path("", PollListView.as_view(), name="poll-list"),
    path("create/", PollCreateView.as_view(), name="poll-create"),
    path("<int:id>/", PollDetailView.as_view(), name="poll-detail"),
    path("vote/", VoteCreateView.as_view(), name="vote")
]
