from rest_framework import serializers
from residences.models import *


# Policies serializer
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ('id', 'title', 'description', 'is_valid', 'created_time', 'modified_time')


# Facilities serializer
class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('id', 'title', 'description', 'is_valid', 'created_time', 'modified_time')


# Image-related serializers
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'title', 'description', 'avatar', 'album', 'is_valid', 'created_time', 'modified_time')


class ImageAlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, allow_null=True)

    class Meta:
        model = ImageAlbum
        fields = ('id', 'title', 'description', 'images', 'is_valid', 'created_time', 'modified_time')


# Location-related serializers
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'title', 'is_valid', 'country', 'created_time', 'modified_time')
        extra_kwargs = {
            'country': {'allow_null': True}
        }


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, allow_null=True)

    class Meta:
        model = Country
        fields = ('id', 'title', 'is_valid', 'cities', 'created_time', 'modified_time')


# Unit serializer
class UnitSerializer(serializers.ModelSerializer):
    image_album = ImageAlbumSerializer(many=False)
    facilities = FacilitySerializer(many=True)
    policies = PolicySerializer(many=True)

    class Meta:
        model = Unit
        fields = ('id', 'title', 'description', 'capacity', 'bedroom', 'bed', 'image_album', 'facilities', 'policies'
                  , 'is_valid', 'created_time', 'modified_time')


# Residences serializers
class HotelSerializer(serializers.ModelSerializer):
    image_album = ImageAlbumSerializer(many=False, allow_null=True)
    units = UnitSerializer(many=True, allow_null=True)
    facilities = FacilitySerializer(many=True, allow_null=True)
    policies = PolicySerializer(many=True, allow_null=True)

    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'capacity', 'image_album', 'units', 'facilities', 'policies',
                  'city', 'is_valid', 'created_time', 'modified_time')


class ResidenceSerializer(serializers.ModelSerializer):
    images = ImageAlbumSerializer(many=False)
    facility = FacilitySerializer(many=True)
    policy = PolicySerializer(many=True)

    class Meta:
        model = Residence
        fields = ('id', 'title', 'description', 'capacity', 'bedroom', 'bed', 'images', 'facility', 'policy',
                  'city', 'is_valid', 'created_time', 'modified_time')
























