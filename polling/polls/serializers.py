from rest_framework import serializers
from .models import Poll


class PollSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=300)
    body = serializers.CharField(max_length=300)
    is_public = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField()

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.is_public = validated_data.get("is_public", instance.is_public)
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ["id", "title", "body", "is_public", "created_at", "last_modified"]
