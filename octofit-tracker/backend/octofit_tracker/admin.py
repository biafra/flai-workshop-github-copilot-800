from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'team', 'total_points']
    search_fields = ['name', 'email', 'team']
    list_filter = ['team']
    ordering = ['-total_points']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'total_points', 'member_count']
    search_fields = ['name', 'description']
    ordering = ['-total_points']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'activity_type', 'duration', 'points', 'date']
    search_fields = ['user_email', 'activity_type']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'name', 'team', 'points']
    search_fields = ['name', 'team']
    list_filter = ['team']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'duration', 'points', 'category']
    search_fields = ['name', 'description', 'category']
    list_filter = ['difficulty', 'category']
    ordering = ['name']
