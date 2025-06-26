from rest_framework.test import APIRequestFactory
from ...common import ExistingReplyTestCase
from ....serializers.replies import ReplyDisplaySerializer
from django.contrib.auth.models import AnonymousUser

class DisplayReplySerializerTest(ExistingReplyTestCase):
    def setUp(self):
        super().setUp()

        self.factory = APIRequestFactory()

    def test_authenticated_user(self):
        request = self.factory.get("/")
        request.user = self.user

        serializer = ReplyDisplaySerializer(
            instance=self.reply, 
            context={'request': request})
        
        data = serializer.data

        self.assertTrue(data["can_edit"])

    def test_unauthenticated_user(self):
        request = self.factory.get("/")
        request.user = AnonymousUser() # non-logged in user

        serializer = ReplyDisplaySerializer(
            instance=self.reply, 
            context={'request': request})
        
        data = serializer.data

        self.assertFalse(data["can_edit"])
