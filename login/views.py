import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from .serializers import UserTokenObtainPairSerializer, RegisterSerializer, ChangeUsernameSerializer, ChangePasswordSerializer

User = get_user_model()

def index(request):
    return HttpResponse("Login Test")

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ChangeUsernameView(generics.UpdateAPIView):
    serializer_class = ChangeUsernameSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
        "role": "mod" if user.is_superuser else "user"
    })

