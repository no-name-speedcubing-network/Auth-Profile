from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse

from ..models import ProfileResults, UserProfile
from django.contrib.auth.models import User
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()

        user = User(email="example@gmail.com", username="Anton")
        user.set_password("1234567")
        user.save()

    def test_users_GET(self):
        response = self.client.get('/api/users/1/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, {"username": "Anton", "email": "example@gmail.com"})

    def test_users_POST(self):
        response = self.client.post('/api/users/', {"username": "My_username", "email": "mymail@gmail.com",
                                                    "password": "12345678"}, format='json')
        # expected = User.objects.get(username='Anton')
        self.assertEquals(response.status_code, 201)

