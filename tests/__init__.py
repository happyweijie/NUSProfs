from django.core.cache import cache

# Patch delete_pattern to avoid errors in tests
if not hasattr(cache, 'delete_pattern'):
    cache.delete_pattern = lambda pattern, *args, **kwargs: None
