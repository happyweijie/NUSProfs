from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

class LikeToggleView(APIView): # Generic view for toggling likes on reviews and replies
    permission_classes = [permissions.IsAuthenticated]
    model = None

    def post(self, request, pk):
        if not self.model:
            return Response({"detail": "Model not specified."}, status=500)
        
        obj = get_object_or_404(self.model, pk=pk)
        user = request.user

        if user in obj.likes.all():
            obj.likes.remove(user)
            liked = False
        else:
            obj.likes.add(user)
            liked = True

        return Response({
            "liked": liked, 
            "likes_count": obj.likes.count()
        }, status=status.HTTP_200_OK)
    