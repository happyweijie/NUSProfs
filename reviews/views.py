from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from .serializers import ReviewSerializer
from .models import Review, Reply

# Create your views here.
def index(request):
    return HttpResponse("Test")

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to edit their own reviews
        return Review.objects.filter(user_id=self.request.user)

# def reply

# def like