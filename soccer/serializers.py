from rest_framework import serializers

from .models import Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    team_string = serializers.CharField(source='team.name')

    class Meta:
        model = Player
        fields = ('pk', 'name', 'team', 'team_string')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('pk', 'name')
