from rest_framework import generics

# from django.contrib.auth.models import User
from polling.users.models import User
from polling.users.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]
    lookup_field = "id"
