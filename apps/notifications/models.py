from django.db import models
from django.utils import timezone
from accounts.models import User  

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{'READ' if self.is_read else 'UNREAD'}] {self.title} ({self.user.username})"
