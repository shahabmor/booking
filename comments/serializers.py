from rest_framework import serializers
from django.db.utils import IntegrityError
from .models import *


# -------------------------------------------------comment--------------------------------------------------------------
# Residence Comment Serializer------------------------------------------------------------------------------------------
class ResidenceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceComment
        fields = ['id', 'user', 'comment_body', 'residence', 'parent']

        extra_kwargs = {
            'parent': {'required': False, 'allow_null': True},
            'user': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(ResidenceCommentSerializer, self).create(validated_data)


# Hotel Comment Serializer----------------------------------------------------------------------------------------------
class HotelCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelComment
        fields = ['id', 'user', 'comment_body', 'hotel', 'parent']

        extra_kwargs = {
            'parent': {'required': False, 'allow_null': True},
            'user': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(HotelCommentSerializer, self).create(validated_data)


# AirPlane Ticket Comment Serializer------------------------------------------------------------------------------------
class AirPlaneTicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneTicketComment
        fields = ['id', 'user', 'comment_body', 'airplane_ticket', 'parent']

        extra_kwargs = {
            'parent': {'required': False, 'allow_null': True},
            'user': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(AirPlaneTicketCommentSerializer, self).create(validated_data)


# --------------------------------------------------rate----------------------------------------------------------------
# Residence Rating Serializer-------------------------------------------------------------------------------------------
class ResidenceRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceRating
        fields = ['id', 'user', 'rate', 'residence']

        extra_kwargs = {
            'user': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        try:
            return super(ResidenceRatingSerializer, self).create(validated_data)

        except IntegrityError:
            return ResidenceRating.objects.get(user=user, residence=validated_data['residence'])


# Hotel Rating Serializer-----------------------------------------------------------------------------------------------
class HotelRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRating
        fields = ['id', 'user', 'rate', 'hotel']

        extra_kwargs = {
            'user': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        try:
            return super(HotelRatingSerializer, self).create(validated_data)

        except IntegrityError:
            return HotelRating.objects.get(user=user, hotel=validated_data['hotel'])


# AirPlane Rating Serializer-----------------------------------------------------------------------------------------------
class AirPlaneTicketRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneTicketRating
        fields = ['id', 'user', 'rate', 'airplane_ticket']

        extra_kwargs = {
            'user': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        try:
            return super(AirPlaneTicketRatingSerializer, self).create(validated_data)

        except IntegrityError:
            return AirplaneTicketRating.objects.get(user=user, airplane_ticket=validated_data['airplane_ticket'])

