import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserTokenObtainPairSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

User = get_user_model()

# Create your views here.
def index(request):
    return HttpResponse("Hello")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
        "role": "mod" if user.is_superuser else "user"
    })
