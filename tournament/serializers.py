from rest_framework import serializers

from .models import Participant, Tournament


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ('pk', 'name', 'tournament')


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('pk', 'name')
