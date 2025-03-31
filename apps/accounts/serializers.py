# serializers.py
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    """
    Registration serializer with:
      - username (required)
      - password1 (required)
      - password2 (required)
      - first_name (optional)
      - last_name (optional)
      - image (optional)
    """
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'image',
            'password1',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords didn't match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    For retrieving/updating user info (including optional fields like phone_number, address).
    Some fields are read-only.
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'image',
            'date_joined'
        ]
        read_only_fields = ['id', 'username', 'date_joined']


class PasswordChangeSerializer(serializers.Serializer):
    """
    For changing the password.
    """
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['new_password1'] != attrs['new_password2']:
            raise serializers.ValidationError({"password": "New passwords didn't match."})
        return attrs
