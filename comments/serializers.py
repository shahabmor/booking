from rest_framework import serializers
from .models import *

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

