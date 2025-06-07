# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    supabase_id = models.CharField(max_length=255, unique=True)  # Supabase UID (JWT 'sub')
    photo_url = models.URLField(blank=True, null=True)
    role = models.CharField(max_length=20, default='user')  # Example custom field

    def __str__(self):
        return self.email