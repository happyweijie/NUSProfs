from ...models import Review
from ..common import LikeToggleView
    
class ReviewLikeToggleView(LikeToggleView):
    model = Review