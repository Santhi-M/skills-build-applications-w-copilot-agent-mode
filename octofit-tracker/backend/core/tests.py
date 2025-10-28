
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Activity, Team, Workout, Leaderboard

class APISmokeTests(APITestCase):
	def test_api_root(self):
		url = reverse('api_root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_users_list(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_activities_list(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_teams_list(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_workouts_list(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_leaderboards_list(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
