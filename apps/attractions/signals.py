# attractions/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Feedback, Attraction

def _update_attraction_rating(attraction):
    """
    Helper function to recalculate the average rating of the given attraction.
    """
    feedbacks = attraction.feedbacks.all()
    if feedbacks.exists():
        total_rating = sum(fb.rating for fb in feedbacks)
        attraction.average_rating = total_rating / feedbacks.count()
    else:
        attraction.average_rating = 0.0
    attraction.save()

@receiver(post_save, sender=Feedback)
def update_attraction_rating_on_save(sender, instance, **kwargs):
    _update_attraction_rating(instance.attraction)

@receiver(post_delete, sender=Feedback)
def update_attraction_rating_on_delete(sender, instance, **kwargs):
    _update_attraction_rating(instance.attraction)
