from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from ..serializers import ChangeUsernameSerializer

User = get_user_model()

class ChangeUsernameView(generics.UpdateAPIView):
    serializer_class = ChangeUsernameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    