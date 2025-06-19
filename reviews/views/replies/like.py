from ...models import Reply
from ..common import LikeToggleView

class ReplyLikeToggleView(LikeToggleView):
    model = Reply