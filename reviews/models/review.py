from django.db import models
from login.models import CustomUser
from professors.models import Professor, Module
from .comment import Comment

class Review(Comment):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    prof_id = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reviews')
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    rating = models.FloatField(default=0.0)
    likes = models.ManyToManyField(CustomUser, related_name='liked_reviews', blank=True)
