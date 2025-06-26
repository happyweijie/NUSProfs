from ...common import ExistingReviewTestCase
from rest_framework import status
from django.urls import reverse

class DeleteReviewTest(ExistingReviewTestCase):
    def setUp(self):
        super().setUp()

        self.reply_content = {
            "review_id": self.review.id,
            "text": "Nice!"
        }

        self.url = reverse("reviews:create_reply", args=[self.review.id])

    def test_owner_create_reply(self):
        response = self.client.post(self.url, self.reply_content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.review.reply_count(), 1)

    def test_unauthorized_reply(self):
        self.client.credentials()
        response = self.client.post(self.url, self.reply_content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)