from rest_framework import serializers
from .models import Poll, Vote


class PollSerializer(serializers.ModelSerializer):

    average_votes = serializers.ReadOnlyField()

    class Meta:
        model = Poll
        fields = ["title", "body", "is_public", "created_at", "average_votes", "creator"]


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = "__all__"
