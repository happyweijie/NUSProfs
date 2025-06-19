from rest_framework import generics, permissions
from ...models import Reply

class ReplyDeleteView(generics.DestroyAPIView):
    queryset = Reply.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Staff can delete any reply
        if self.request.user.is_staff:
            return Reply.objects.all()
        # Only allow users to delete their own replies
        return Reply.objects.filter(user_id=self.request.user)
    