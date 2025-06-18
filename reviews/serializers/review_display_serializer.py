from .comment_display_serializer import CommentDisplaySerializer
from ..models import Review

class ReviewDisplaySerializer(CommentDisplaySerializer):

    class Meta(CommentDisplaySerializer.Meta):
        model = Review
        fields = CommentDisplaySerializer.Meta.fields + [
            'prof_id', 'module_code', 'rating'
        ]
