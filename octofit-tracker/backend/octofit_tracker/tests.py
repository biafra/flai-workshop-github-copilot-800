from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            team="Test Team",
            total_points=100
        )
    
    def test_get_users_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'team': 'Team A',
            'total_points': 0
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITestCase(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team",
            total_points=500,
            member_count=5
        )
    
    def test_get_teams_list(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        url = reverse('team-list')
        data = {
            'name': 'New Team',
            'description': 'A new team',
            'total_points': 0,
            'member_count': 0
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITestCase(APITestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="test@example.com",
            activity_type="Running",
            duration=30,
            points=50
        )
    
    def test_get_activities_list(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {
            'user_email': 'test2@example.com',
            'activity_type': 'Cycling',
            'duration': 45,
            'points': 75
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITestCase(APITestCase):
    def setUp(self):
        self.leaderboard_entry = Leaderboard.objects.create(
            rank=1,
            name="Top User",
            team="Team A",
            points=1000
        )
    
    def test_get_leaderboard_list(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_leaderboard_entry(self):
        url = reverse('leaderboard-list')
        data = {
            'rank': 2,
            'name': 'Second User',
            'team': 'Team B',
            'points': 900
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class WorkoutAPITestCase(APITestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run",
            difficulty="Medium",
            duration=30,
            points=50,
            category="Cardio"
        )
    
    def test_get_workouts_list(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {
            'name': 'Evening Yoga',
            'description': 'Relaxing evening yoga session',
            'difficulty': 'Easy',
            'duration': 45,
            'points': 40,
            'category': 'Flexibility'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class APIRootTestCase(APITestCase):
    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
