from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ...serializers import RegisterSerializer

User = get_user_model()

class RegisterSerializerTest(APITestCase):
    def test_valid_data_creates_user(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "StrongPass123",
            "confirm_password": "StrongPass123",
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.username, data["username"])
        self.assertEqual(user.email, data["email"])

    def test_missing_username(self):
        data = {
            "username": "",
            "email": "test@example.com",
            "password": "password",
            "confirm_password": "password"
            }
        self.assertFalse(RegisterSerializer(data=data).is_valid())

    def test_weak_password(self):
        data = {
            "username": "abc",
            "email": "test@example.com",
            "password": "password",
            "confirm_password": "password"
            }
        
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_duplicate_username(self):
        User.objects.create_user(
            username="existing", 
            password="STR0NGPWD!",
            email="existing@example.com"
            )
        
        data = {
            "username": "existing",
            "email": "new@example.com",
            "password": "Somepass123",
            "confirm_password": "Somepass123"
        }

        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)
