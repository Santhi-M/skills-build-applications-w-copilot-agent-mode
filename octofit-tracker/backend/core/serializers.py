from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity, Team, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'teams', 'workouts']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    activity = ActivitySerializer(read_only=True)
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = '__all__'
