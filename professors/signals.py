from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Semester

@receiver(post_save, sender=Semester)
def clear_academic_year_cache(sender, instance, **kwargs):
    cache.delete("academic_year_list")
