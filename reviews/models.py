from django.db import models
from datetime import datetime
from login.models import CustomUser
from professors.models import Professor, Module

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=20000, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.now())

    class Meta:
        abstract = True

class Review(Comment):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    prof_id = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reviews')
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    rating = models.FloatField(default=0.0)
    likes = models.ManyToManyField(CustomUser, related_name='liked_reviews', blank=True)

class Reply(Comment):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='replies')
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='replies')
    likes = models.ManyToManyField(CustomUser, related_name='liked_replies', blank=True)
