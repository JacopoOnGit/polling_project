from rest_framework import serializers
from .models import Poll, Choice, Vote

class ChoiceSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['id', 'text', 'votes_count']

    def get_votes_count(self, obj):
        return obj.votes.count()

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    votes_count = serializers.SerializerMethodField()
    is_owner_or_admin = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'created_at', 'author', 'choices', 'votes_count', 'is_owner_or_admin']
        read_only_fields = ['author', 'created_at', 'choices', 'votes_count', 'is_owner_or_admin']
    def get_votes_count(self, obj):
        return Vote.objects.filter(poll=obj).count()

    def get_is_owner_or_admin(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            return request.user.is_authenticated and (obj.author == request.user or request.user.is_staff)
        return False

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'poll', 'choice', 'user', 'voted_at']
        read_only_fields = ['user', 'voted_at']

