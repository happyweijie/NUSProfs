from .existing_review_test import ExistingReviewTestCase
from ...models import Reply

class ExistingReplyTestCase(ExistingReviewTestCase):
    def setUp(self):
        super().setUp()

        self.reply = Reply.objects.create(
            user_id=self.user,
            review_id=self.review,
            text="test",
        )
        