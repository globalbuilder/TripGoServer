from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from documentation import APIDocumentationView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('attractions.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api-docs/', APIDocumentationView.as_view(), name='api-docs'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
