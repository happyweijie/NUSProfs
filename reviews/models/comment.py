from django.db import models
from django.utils import timezone

class Comment(models.Model):
    text = models.CharField(max_length=20000, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
