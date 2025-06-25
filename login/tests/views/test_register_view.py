from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterViewTest(APITestCase):
    def setUp(self):
        self.url = reverse("login:register")  # Update this to match your `urls.py` name

    def test_register_success(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Testpass123",
            "confirm_password": "Testpass123",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_register_missing_fields(self):
        data = {
            "username": "incomplete"
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
        self.assertIn("confirm_password", response.data)

    def test_register_existing_user(self):
        User.objects.create_user(username="testuser", password="abc123", email="test@example.com")
        data = {
            "username": "testuser",
            "email": "duplicate@example.com",
            "password": "Anotherpass123",
            "confirm_password": "Anotherpass123"
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)
