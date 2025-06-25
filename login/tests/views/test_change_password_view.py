from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class ChangePasswordViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="OldPass123")   
        self.url = reverse("login:change_password")

        # generate token
        self.client.login(username="user", password="OldPass123")
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # authenticate client
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_success(self):
        data = {
            "old_password": "OldPass123",
            "new_password": "NewSecurePass456",
            "confirm_password": "NewSecurePass456"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("NewSecurePass456"))

    def test_wrong_old_password(self):
        data = {
            "old_password": "WrongPass",
            "new_password": "NewPass123",
            "confirm_password": "NewPass123"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("OldPass123"))

    def test_password_mismatch(self):
        data = {
            "old_password": "OldPass123",
            "new_password": "NewPass123",
            "confirm_password": "NewPass1234"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("OldPass123"))

    def test_unauthenticated(self):
        self.client.logout()
        data = {
            "old_password": "OldPass123",
            "new_password": "NewPass123",
            "confirm_password": "NewPass123"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
