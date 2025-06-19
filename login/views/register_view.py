from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from ..serializers import RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
