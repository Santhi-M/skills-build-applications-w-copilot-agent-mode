from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    duration = models.IntegerField(help_text="Duration in minutes")
    points_earned = models.IntegerField(default=0)
    completed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity.name}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField()
    last_calculated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.total_points} points"

    class Meta:
        ordering = ['-total_points']
