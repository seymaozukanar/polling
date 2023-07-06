from django.urls import path

from polling.users.views import UserListView, UserDetailView
from polling.users.models import User
from polling.users.serializers import UserSerializer


urlpatterns = [
    path("", UserListView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name="user-list"),
    path("<int:id>/", UserDetailView.as_view(), name="user-detail")
]
