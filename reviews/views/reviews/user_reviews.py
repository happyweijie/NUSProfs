from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from ...serializers.reviews import (
    ReviewDisplaySerializer, 
)
from ...models import Review

User = get_user_model()

class UserReviewListView(generics.ListAPIView):
    serializer_class = ReviewDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        if username:
            user = get_object_or_404(User, username=username)
        else:
            user = self.request.user  # View own reviews

        return Review.objects.filter(user_id=user).order_by('-timestamp')
    