# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address',
        'image_tag',
        'is_staff',
        'date_joined',
        'last_login'
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'phone_number',
                'address',
                'image'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    def image_tag(self, obj):
        """Display a small thumbnail of the user's image in the admin list."""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:50px; max-width:50px;" />', 
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'
