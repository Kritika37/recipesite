from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Recipe

@receiver(post_save, sender=Recipe)
def clear_cache_on_save(sender, instance, **kwargs):
    """
    Clears the cache for this recipe when it’s created or updated.
    """
    cache_key = f"recipe_{instance.id}"
    cache.delete(cache_key)
    print(f"🧹 Cache cleared for recipe {instance.id} after save/update.")

@receiver(post_delete, sender=Recipe)
def clear_cache_on_delete(sender, instance, **kwargs):
    """
    Clears the cache for this recipe when it’s deleted.
    """
    cache_key = f"recipe_{instance.id}"
    cache.delete(cache_key)
    print(f"🧹 Cache cleared for recipe {instance.id} after delete.")
