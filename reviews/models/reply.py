from django.db import models
from login.models import CustomUser
from .comment import Comment
from .review import Review

class Reply(Comment):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='replies')
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='replies')
    likes = models.ManyToManyField(CustomUser, related_name='liked_replies', blank=True)

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"
