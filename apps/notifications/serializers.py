# apps/notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Notification
        fields = [
            'id',
            'user',
            'user_username',
            'is_broadcast',
            'title',
            'message',
            'created_at'
        ]
        read_only_fields = ['created_at', 'user']
