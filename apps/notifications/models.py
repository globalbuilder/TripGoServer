# apps/notifications/models.py
from django.db import models
from django.utils import timezone
from accounts.models import User

class Notification(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='notifications',
        null=True, 
        blank=True
    )
    is_broadcast = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        if self.is_broadcast:
            return f"[Broadcast] {self.title}"
        return f"[User: {self.user.username}] {self.title}"
