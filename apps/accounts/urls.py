# urls.py
from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    PasswordChangeView,
    UserRetrieveUpdateView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(), name='change-password'),
    path('me/', UserRetrieveUpdateView.as_view(), name='user-info'),
]
