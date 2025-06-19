from rest_framework import generics, permissions
from ...serializers.replies import (
    ReplyDisplaySerializer,
)
from ...models import Reply

class ReplyDisplayView(generics.ListAPIView):
    serializer_class = ReplyDisplaySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        return Reply.objects.filter(review_id=review_id).order_by('-timestamp')
    