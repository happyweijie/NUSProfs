from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReviewSerializer, ReplySerializer, ReplyUpdateSerializer 
from .models import Review, Reply

# Create your views here.
def index(request):
    return HttpResponse("Test")

# Reviews
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to edit their own reviews
        return Review.objects.filter(user_id=self.request.user)

class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Staff can delete any review
        if self.request.user.is_staff:
            return Review.objects.all()
        # Only allow users to delete their own reviews
        return Review.objects.filter(user_id=self.request.user)
    
# Replies
class ReplyCreateView(generics.CreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated]

class ReplyUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReplyUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to edit their own replies
        return Reply.objects.filter(user_id=self.request.user)

class ReplyDeleteView(generics.DestroyAPIView):
    queryset = Reply.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Staff can delete any reply
        if self.request.user.is_staff:
            return Reply.objects.all()
        # Only allow users to delete their own replies
        return Reply.objects.filter(user_id=self.request.user)
    
# Likes
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
    
class ReviewLikeToggleView(LikeToggleView):
    model = Review

class ReplyLikeToggleView(LikeToggleView):
    model = Reply
