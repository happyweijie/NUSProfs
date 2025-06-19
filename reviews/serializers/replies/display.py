from ..common import CommentDisplaySerializer
from ...models import Reply

class ReplyDisplaySerializer(CommentDisplaySerializer):

    class Meta(CommentDisplaySerializer.Meta):
        model = Reply
        fields = CommentDisplaySerializer.Meta.fields + [
            'review_id'
        ]
