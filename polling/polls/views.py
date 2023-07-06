from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from polling.pagination import SmallPagesPagination
from polling.polls.models import Poll
from polling.polls.serializers import PollSerializer, VoteSerializer


class PollCreateView(CreateAPIView):
    serializer_class = PollSerializer
    lookup_field = "id"


class PollListView(ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = "id"
    pagination_class = SmallPagesPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at",]


class PollDetailView(RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = "id"


class VoteCreateView(CreateAPIView):
    serializer_class = VoteSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
