from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class ChangeUsernameViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="original", password="Pass1234")
        self.url = reverse("login:change_username") 

        # Generate tokens
        self.client.login(username="original", password="Pass1234")
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # authenticated client
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_change_username_success(self):
        response = self.client.put(self.url, {"username": "updated"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "updated")

    def test_change_username_to_existing(self):
        User.objects.create_user(username="taken", password="OtherPass")
        response = self.client.put(self.url, {"username": "taken"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_username_unauthenticated(self):
        self.client.credentials()  # Remove JWT auth header
        response = self.client.put(self.url, {"username": "hacker"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
