from django.db import models
from datetime import datetime
from login.models import CustomUser

# Create your models here.
class Comment(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=20000, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.now())