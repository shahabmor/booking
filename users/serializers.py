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



