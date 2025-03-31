# attractions/serializers.py

from rest_framework import serializers
from .models import Category, Attraction, Feedback, Favorite

class CategorySerializer(serializers.ModelSerializer):
    """
    For listing/retrieving categories. 
    We can also show the total attractions in each category if desired.
    """
    attractions_count = serializers.IntegerField(source='attractions.count', read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'image',
            'attractions_count',
            'created_at',
            'updated_at'
        ]


class AttractionSerializer(serializers.ModelSerializer):
    """
    For listing/retrieving attractions, including average_rating.
    """
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Attraction
        fields = [
            'id',
            'category',
            'category_name',
            'name',
            'latitude',
            'longitude',
            'address',
            'description',
            'image',
            'price',
            'average_rating',
            'created_at',
            'updated_at',
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    """
    For creating and retrieving feedback.
    `user` is read-only in typical scenarios (taken from request).
    """
    user_username = serializers.ReadOnlyField(source='user.username')
    attraction_name = serializers.ReadOnlyField(source='attraction.name')

    class Meta:
        model = Feedback
        fields = [
            'id',
            'user',
            'user_username',
            'attraction',
            'attraction_name',
            'rating',
            'comment',
            'created_at'
        ]
        read_only_fields = ['user', 'created_at']


class FavoriteSerializer(serializers.ModelSerializer):
    """
    For marking/unmarking favorites.
    """
    user_username = serializers.ReadOnlyField(source='user.username')
    attraction_name = serializers.ReadOnlyField(source='attraction.name')

    class Meta:
        model = Favorite
        fields = [
            'id',
            'user',
            'user_username',
            'attraction',
            'attraction_name',
            'created_at'
        ]
        read_only_fields = ['user', 'created_at']
