from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LogoutViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="StrongPass123")
        self.client = APIClient()
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh.access_token}")
        self.url = reverse("login:logout") 

    def test_logout_success(self):
        response = self.client.post(self.url, {"refresh": str(self.refresh)})
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_logout_unauthorized(self):
        self.client.credentials()  # remove auth
        response = self.client.post(self.url, {"refresh": str(self.refresh)})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
