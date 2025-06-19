from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

User = get_user_model()
    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
        "role": "mod" if user.is_superuser else "user"
    })
