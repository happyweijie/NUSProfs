from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import UserTokenObtainPairSerializer

User = get_user_model()

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
