from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):

    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

class NotificationDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
