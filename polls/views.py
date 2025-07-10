from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.author != user and not user.is_staff:
            raise PermissionDenied("⛔ Solo l'autore o un admin può cancellare questo sondaggio.")
        instance.delete()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def perform_create(self, serializer):
        poll = serializer.validated_data['poll']
        user = self.request.user
        if poll.author != user:
            raise PermissionDenied("⛔ Non puoi aggiungere scelte a sondaggi non tuoi.")
        serializer.save()

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        poll = serializer.validated_data['poll']
        user = self.request.user

        # Se l'utente ha già votato, aggiorna il voto
        existing_vote = Vote.objects.filter(poll=poll, user=user).first()
        if existing_vote:
            existing_vote.choice = serializer.validated_data['choice']
            existing_vote.save()
        else:
            serializer.save(user=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
