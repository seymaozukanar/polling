import json
from rest_framework import serializers
from polling.polls.models import Poll, Vote


class PollSerializer(serializers.ModelSerializer):

    average_votes = serializers.ReadOnlyField()
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ["title", "body", "is_public", "created_at", "average_votes", "creator", "votes"]

    # allow only the creator of polls to see vote details
    def get_votes(self, obj):
        if obj.creator.id == self.context["request"].user.id and obj.is_public == True:
            queryset =  Vote.objects.filter(poll_id=obj.id)
            return json.dumps([dict(item) for item in queryset.values("user", "value")])
        return None


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = "__all__"
