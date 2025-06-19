from rest_framework import generics, permissions
from ...serializers.replies import (
    ReplyUpdateSerializer
)
from ...models import Reply

class ReplyUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReplyUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to edit their own replies
        return Reply.objects.filter(user_id=self.request.user)
