# apps/notifications/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from attractions.models import Attraction
from .models import Notification

@receiver(post_save, sender=Attraction)
def broadcast_new_attraction_notification(sender, instance, created, **kwargs):
    if created:
        # A new Attraction has been created
        Notification.objects.create(
            is_broadcast=True,
            title="New Attraction Added",
            message=f"A new attraction '{instance.name}' has been added!"
        )
