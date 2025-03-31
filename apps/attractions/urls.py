# attractions/urls.py

from django.urls import path
from .views import (
    # Categories
    CategoryListView,
    CategoryAttractionsListView,

    # Attractions
    AttractionListView,
    AttractionDetailView,

    # Feedback
    FeedbackCreateView,
    FeedbackDeleteView,

    # Favorites
    AddFavoriteView,
    RemoveFavoriteView,
    FavoriteListView
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/attractions/', CategoryAttractionsListView.as_view(), name='category-attractions'),

    # Attractions
    path('attractions/', AttractionListView.as_view(), name='attraction-list'),
    path('attractions/<int:pk>/', AttractionDetailView.as_view(), name='attraction-detail'),

    # Feedback
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/<int:pk>/', FeedbackDeleteView.as_view(), name='feedback-delete'),

    # Favorites
    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/add/', AddFavoriteView.as_view(), name='favorite-add'),
    path('favorites/remove/', RemoveFavoriteView.as_view(), name='favorite-remove'),
]
