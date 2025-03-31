# apps/notifications/views.py

from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    Returns a list of notifications:
    - All broadcast notifications (is_broadcast=True)
    - The user's specific notifications (user=request.user)
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(
            is_broadcast=True
        ) | Notification.objects.filter(
            user=self.request.user
        ).order_by('-created_at')


class NotificationDetailView(generics.RetrieveAPIView):
    """
    Returns a single notification detail if it's broadcast or 
    if the current user is the owner.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_object(self):
        notification_id = self.kwargs['pk']
        notification = get_object_or_404(Notification, pk=notification_id)
        # Check if it's broadcast or belongs to the user
        if notification.is_broadcast or notification.user == self.request.user:
            return notification
        else:
            # If user is not the owner (and it's not broadcast), deny access
            raise PermissionError("Not allowed to view this notification.")
