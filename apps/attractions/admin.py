# attractions/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Attraction, Feedback, Favorite

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_tag', 'created_at', 'updated_at')
    search_fields = ('name',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px; max-width:50px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'category', 'image_tag', 
        'average_rating', 'created_at', 'updated_at'
    )
    list_filter = ('category',)
    search_fields = ('name', 'address')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px; max-width:50px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'attraction', 'rating', 'created_at')
    list_filter = ('rating', 'attraction')
    search_fields = ('user__username', 'attraction__name', 'comment')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'attraction', 'created_at')
    list_filter = ('user', 'attraction')
    search_fields = ('user__username', 'attraction__name')
