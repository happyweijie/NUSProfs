from rest_framework import generics, permissions
from ...models import Review 

class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Staff can delete any review
        if self.request.user.is_staff:
            return Review.objects.all()
        # Only allow users to delete their own reviews
        return Review.objects.filter(user_id=self.request.user)
    