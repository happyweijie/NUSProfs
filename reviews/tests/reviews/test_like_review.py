from .common import ExistingReviewTestCase
from ...models import Review
from rest_framework import status
from django.urls import reverse

class LikeReviewTest(ExistingReviewTestCase):
    def setUp(self):
        super().setUp()

        self.url = reverse("reviews:like_review", args=[self.review.id])

    def test_like_and_unlike_review(self):
        # like review
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user, self.review.likes.all())
        self.assertEqual(response.data["liked"], True)
        self.assertEqual(response.data["likes_count"], 1)

    def test_unlike_review(self):
        # un-like review
        self.client.post(self.url)
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(self.user, self.review.likes.all())
        self.assertEqual(response.data["liked"], False)
        self.assertEqual(response.data["likes_count"], 0)

    def test_unauthorized_likes_review(self):
        self.client.credentials()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
