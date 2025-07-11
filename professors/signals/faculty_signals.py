from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from ..models import Faculty, Department  # Adjust path if needed

@receiver([post_save, post_delete], sender=Faculty)
@receiver([post_save, post_delete], sender=Department)
def clear_faculty_cache(sender, **kwargs):
    cache.delete("faculty_list")
