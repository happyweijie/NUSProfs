from rest_framework import generics, permissions
from ...serializers.reviews import (
    ReviewDisplaySerializer, 
)
from ...models import Review

class ProfessorReviewsView(generics.ListAPIView):
    serializer_class = ReviewDisplaySerializer
    permission_classes = [permissions.AllowAny]

    # show latest reviews for a specific professor
    def get_queryset(self):
        prof_id = self.kwargs['prof_id']
        return Review.objects.filter(prof_id=prof_id).order_by('-timestamp')
    