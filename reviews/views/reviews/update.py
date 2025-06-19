from rest_framework import generics, permissions
from ...serializers.reviews import (
    ReviewUpdateSerializer, 
)
from ...models import Review

class ReviewUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReviewUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to edit their own reviews
        return Review.objects.filter(user_id=self.request.user)
