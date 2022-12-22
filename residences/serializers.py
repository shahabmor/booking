from rest_framework import serializers
from residences.models import *


# Rent-related serializer-----------------------------------------------------------------------------------------------
class RentResidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentResidence
        fields = ('id', 'date', 'residence', 'user')
        extra_kwargs = {'residence': {'allow_null': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(RentResidenceSerializer, self).create(validated_data)


class RentHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentHotel
        fields = ('id', 'date', 'unit', 'user')
        extra_kwargs = {
            'unit': {'allow_null': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(RentHotelSerializer, self).create(validated_data)


# Facility serializer-------------------------------------------------------------------------------------------------
class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('id', 'title', 'description', 'hotel', 'residence', 'unit',
                  'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {
            'residence': {'required': False, 'allow_null': True},
            'hotel': {'required': False, 'allow_null': True},
            'unit': {'required': False, 'allow_null': True},
        }


# Policy serializer---------------------------------------------------------------------------------------------------
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ('id', 'title', 'description', 'residence', 'hotel', 'residence',
                  'is_valid', 'created_time', 'modified_time')

        extra_kwargs = {
            'residence': {'required': False, 'allow_null': True},
            'hotel': {'required': False, 'allow_null': True},
        }


# Price-related serializers---------------------------------------------------------------------------------------------
class PriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceInfo
        fields = ('currency', 'price', 'unit', 'residence')
        extra_kwargs = {
            'unit': {'required': False, 'allow_null': True},
            'residence': {'required': False, 'allow_null': True}
        }

# Image-related serializers---------------------------------------------------------------------------------------------
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'title', 'description', 'avatar', 'album', 'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {'album': {'required': False, 'allow_null': True}}

class ImageAlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ImageAlbum
        fields = ('id', 'title', 'description', 'residence', 'hotel', 'images',
                  'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {
            'residence': {'required': False, 'allow_null': True},
            'hotel': {'required': False, 'allow_null': True}
        }


# Residences serializers------------------------------------------------------------------------------------------------
class UnitSerializer(serializers.ModelSerializer):
    facilities = FacilitySerializer(many=True, read_only=True)
    price_info = PriceInfoSerializer(many=False, read_only=True)

    class Meta:
        model = Unit
        fields = ('id', 'title', 'description', 'capacity', 'bedroom', 'bed', 'hotel',
                  'facilities', 'price_info', 'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {'hotel': {'required': True, 'allow_null': True}}


class ResidenceSerializer(serializers.ModelSerializer):
    image_album = ImageAlbumSerializer(many=False, read_only=True)
    facilities = FacilitySerializer(many=True, read_only=True)
    policies = PolicySerializer(many=True, read_only=True)
    price_info = PriceInfoSerializer(many=False, read_only=True)
    rented_days = RentResidenceSerializer(many=True, read_only=True)

    class Meta:
        model = Residence
        fields = ('id', 'title', 'description', 'capacity', 'bedroom', 'bed', 'city',
                  'image_album', 'facilities', 'policies', 'price_info', 'rented_days',
                  'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {'city': {'required': False, 'allow_null': True}}


class HotelSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    image_album = ImageAlbumSerializer(many=False, read_only=True)
    facilities = FacilitySerializer(many=True, read_only=True)
    policies = PolicySerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'capacity', 'units', 'city', 'image_album',
                  'facilities', 'policies', 'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {'city': {'required': False, 'allow_null': True}}


# Location-related serializers------------------------------------------------------------------------------------------
class CitySerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True, read_only=True)
    residences = ResidenceSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'title', 'country', 'hotels', 'residences', 'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {'country': {'required': False, 'allow_null': True}}


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'title', 'is_valid', 'cities', 'created_time', 'modified_time')































