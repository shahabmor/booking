from abc import ABC

from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('address', 'birthday', 'avatar')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password',
                  'email', 'phone_number', 'profile', 'is_staff', 'is_superuser', 'is_active')


# Login-related Serializer----------------------------------------------------------------------------------------------

class PhoneSerializer(serializers.Serializer):
    phone = serializers.IntegerField(required=True,
                                     validators=[RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')])
