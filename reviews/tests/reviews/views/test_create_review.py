from rest_framework import status
from ...common import BaseReviewTestCase
from django.urls import reverse
from reviews.models.review import Review

class ReviewCreateTest(BaseReviewTestCase):
    def setUp(self):
        super().setUp()

        self.review_url = reverse('reviews:create_review') 

    def test_create_review_success(self):
        response = self.client.post(self.review_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)

    def test_create_review_unauthenticated(self):
        self.client.credentials() 
        response = self.client.post(self.review_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
