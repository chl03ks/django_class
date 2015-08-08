from rest_framework import viewsets

from .serializers import ParticipantSerializer, TournamentSerializer
from .models import Participant, Tournament


class ParticipantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
