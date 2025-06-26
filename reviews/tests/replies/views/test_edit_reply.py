from django.urls import reverse
from rest_framework import status
from ...common import ExistingReplyTestCase

class EditReplyTest(ExistingReplyTestCase):
    def setUp(self):
        super().setUp()

        self.url = reverse("reviews:edit_reply", args=[self.reply.id])

    def test_owner_update_reply(self):
        response = self.client.put(self.url, {"text": "Updated!"})
        self.assertEqual(response.status_code, 200)
        self.reply.refresh_from_db()

        # Checked that content is updated
        self.assertEqual(self.reply.text, "Updated!")

    def test_update_reply_not_owner_fails(self):
        self.client.credentials()
        response = self.client.put(self.url, {"text": "Hacked!"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
