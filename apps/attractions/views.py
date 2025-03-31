# attractions/views.py

from rest_framework import generics, status, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication

from .models import Category, Attraction, Feedback, Favorite
from .serializers import (
    CategorySerializer,
    AttractionSerializer,
    FeedbackSerializer,
    FavoriteSerializer
)

# -------------------------
# 1. Categories
# -------------------------
class CategoryListView(generics.ListAPIView):
    """
    GET a list of all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAttractionsListView(generics.ListAPIView):
    """
    GET attractions belonging to a specific category.
    /api/categories/<pk>/attractions/
    """
    serializer_class = AttractionSerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Attraction.objects.filter(category_id=category_id)


# -------------------------
# 2. Attractions
# -------------------------
class AttractionListView(generics.ListAPIView):
    """
    GET a list of all attractions with search feature (by name).
    Example usage:
      /api/attractions/?search=park
    """
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name'] 


class AttractionDetailView(generics.RetrieveAPIView):
    """
    GET a single attraction by ID.
    """
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


# -------------------------
# 3. Feedback
# -------------------------
class FeedbackCreateView(generics.CreateAPIView):
    """
    POST to create feedback for an attraction.
    The `user` is automatically set to the current authenticated user.
    """
    serializer_class = FeedbackSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedbackDeleteView(APIView):
    """
    DELETE feedback (only if the feedback belongs to the user).
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        feedback = get_object_or_404(Feedback, pk=pk, user=request.user)
        feedback.delete()
        return Response({"message": "Feedback deleted."}, status=status.HTTP_204_NO_CONTENT)


# -------------------------
# 4. Favorites
# -------------------------
class AddFavoriteView(APIView):
    """
    POST to add an attraction to the user's favorites.
    Body example:
      {"attraction": <attraction_id>}
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        attraction_id = request.data.get('attraction')
        if not attraction_id:
            return Response({"error": "Attraction ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        attraction = get_object_or_404(Attraction, pk=attraction_id)
        # Check if already favorited
        favorite, created = Favorite.objects.get_or_create(
            user=request.user, 
            attraction=attraction
        )
        if created:
            return Response({"message": "Added to favorites."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Already in favorites."}, status=status.HTTP_200_OK)


class RemoveFavoriteView(APIView):
    """
    DELETE to remove an attraction from the user's favorites.
    Body example:
      {"attraction": <attraction_id>}
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        attraction_id = request.data.get('attraction')
        if not attraction_id:
            return Response({"error": "Attraction ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        favorite = Favorite.objects.filter(user=request.user, attraction_id=attraction_id).first()
        if favorite:
            favorite.delete()
            return Response({"message": "Removed from favorites."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Favorite not found."}, status=status.HTTP_404_NOT_FOUND)


class FavoriteListView(generics.ListAPIView):
    """
    GET the list of favorite attractions for the logged-in user.
    """
    serializer_class = FavoriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
