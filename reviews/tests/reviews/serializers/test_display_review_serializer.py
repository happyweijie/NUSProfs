from ...common import ExistingReviewTestCase
from rest_framework.test import APIRequestFactory
from ....serializers.reviews import ReviewDisplaySerializer
from django.contrib.auth.models import AnonymousUser

class DisplayReviewSerializerTestCase(ExistingReviewTestCase):
    def setUp(self):
        super().setUp()

        self.factory = APIRequestFactory()

    def test_authenticated_user(self):
        request = self.factory.get("/")
        request.user = self.user

        serializer = ReviewDisplaySerializer(
            instance=self.review, 
            context={'request': request})
        
        data = serializer.data

        self.assertTrue(data["can_edit"])

    def test_unauthenticated_user(self):
        request = self.factory.get("/")
        request.user = AnonymousUser() # non-logged in user

        serializer = ReviewDisplaySerializer(
            instance=self.review, 
            context={'request': request})
        
        data = serializer.data

        self.assertFalse(data["can_edit"])