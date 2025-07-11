from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from ..models import Module

@receiver([post_save, post_delete], sender=Module)
def clear_module_list_cache(sender, **kwargs):
    cache.delete("all_modules_list")
