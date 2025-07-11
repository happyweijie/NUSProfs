from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import Professor, Faculty, Department
from reviews.models import Review
from django.core.cache import cache

@receiver([post_save, post_delete], sender=Professor)
@receiver([post_save, post_delete], sender=Faculty)
@receiver([post_save, post_delete], sender=Department)
@receiver([post_save, post_delete], sender=Review)
def clear_professor_search_cache(sender, **kwargs):
    cache.delete_pattern("professor_search:*")