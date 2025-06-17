from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
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
        # Only allow users to delete their own replies
        return Reply.objects.filter(user_id=self.request.user)
    
# Likes