from ...common import ExistingReviewTestCase
from rest_framework import status
from django.urls import reverse

class EditReviewTestCase(ExistingReviewTestCase):
    def setUp(self):
        super().setUp()

        self.url = reverse('reviews:edit_review', args=[self.review.id])

    def test_owner_update_review(self):
        review = self.review

        # Update Review
        response = self.client.put(self.url, {"rating": 3.0, "text": "Updated!"})
        self.assertEqual(response.status_code, 200)
        review.refresh_from_db()

        # Checked that content is updated
        self.assertEqual(review.rating, 3.0)
        self.assertEqual(review.text, "Updated!")

    def test_update_review_not_owner_fails(self):
        self.client.credentials()
        response = self.client.put(self.url, {"rating": 5.0, "text": "Hacked!"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
