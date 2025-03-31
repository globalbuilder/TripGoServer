# views.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .serializers import (
    RegisterSerializer,
    UserSerializer,
    PasswordChangeSerializer
)

User = get_user_model()

class RegisterView(APIView):
    """
    Creates a new user (registration). 
    """
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Authenticates the user with username & password.
    Returns an auth token if valid.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(
                {"error": "Please provide both username and password."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)
        if user:
            # Get or create the token
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):
    """
    Deletes the user's token, requiring token authentication.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # request.auth is the Token instance if TokenAuthentication is used
        if request.auth:
            request.auth.delete()
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)


class PasswordChangeView(APIView):
    """
    Changes the user's password, requiring valid token authentication.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password1']

            if not user.check_password(old_password):
                return Response(
                    {"error": "Old password is incorrect."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.set_password(new_password)
            user.save()
            return Response(
                {"message": "Password changed successfully."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    Retrieve or update the logged-in user's data.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
