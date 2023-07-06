from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from polling.users.models import User
from polling.users.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]
    lookup_field = "id"
