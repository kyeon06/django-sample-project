from django.urls import reverse
from rest_framework.test import APITestCase

from users.models import User


class LoginAPIViewTestCase(APITestCase):
    def setUp(self):
        self.data = {"username": "testuser2", "password": "testuser2"}
        self.user = User.objects.create_user(username="testuser2", email="testuser2@test.com", password="testuser2")

    def test_login(self):
        url = reverse("user-login")

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 200)
