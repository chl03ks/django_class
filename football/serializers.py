from rest_framework import serializers

from .models import Coach, Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    team_string = serializers.CharField(source='team.name')

    class Meta:
        model = Player
        fields = ('pk', 'name', 'team', 'team_string')


class TeamSerializer(serializers.ModelSerializer):
    coach_name = serializers.CharField(source='coach.name')

    class Meta:
        model = Team
        fields = ('pk', 'name', 'coach', 'coach_name')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('pk', 'name')
