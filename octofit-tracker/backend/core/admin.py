from django.contrib import admin
from .models import Activity, Team, Workout, Leaderboard

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('members',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'duration', 'points_earned', 'completed_at')
    list_filter = ('activity', 'completed_at')
    search_fields = ('user__username', 'activity__name')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'total_points', 'rank', 'last_calculated')
    list_filter = ('team', 'rank')
    search_fields = ('user__username', 'team__name')
