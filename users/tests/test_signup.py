from django.urls import reverse
from rest_framework.test import APITestCase


class SignupAPIViewTestCase(APITestCase):
    def test_signup(self):
        url = reverse("user-signup")
        user_data = {"username": "testuser2", "email": "testuser2@test.com", "password": "testuser2"}

        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)
