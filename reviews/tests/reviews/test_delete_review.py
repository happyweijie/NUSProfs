from ..common import ExistingReviewTestCase
from ...models import Review
from rest_framework import status
from django.urls import reverse

class DeleteReviewTest(ExistingReviewTestCase):
    def setUp(self):
        super().setUp()

        self.url = reverse("reviews:delete_review", args=[self.review.id])

    def test_owner_deletes_review(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)

    def test_unauthorized_delete_review(self):
        self.client.credentials()
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)