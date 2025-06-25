from .base_review_test import BaseReviewTestCase
from ...models import Review

class ExistingReviewTestCase(BaseReviewTestCase):
    """
    Test Case with a Created Review
    """
    def setUp(self):
        super().setUp()

        self.review = Review.objects.create(
            user_id=self.user,
            prof_id=self.jteo,
            module_code=self.module,
            rating=5.0,
            text="Nice!"
        )
