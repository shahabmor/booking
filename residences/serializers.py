from rest_framework import serializers
from residences.models import *


# Facility serializer-------------------------------------------------------------------------------------------------
class ResidenceFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceFacility
        fields = ('id', 'title', 'description', 'residence')
        extra_kwargs = {
            'residence': {'required': False, 'allow_null': True},
        }


class HotelFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFacility
        fields = ('id', 'title', 'description', 'hotel')
        extra_kwargs = {
            'hotel': {'required': False, 'allow_null': True},
        }


class UnitFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitFacility
        fields = ('id', 'title', 'description', 'unit')
        extra_kwargs = {
            'unit': {'required': False, 'allow_null': True},
        }

# Policy serializer---------------------------------------------------------------------------------------------------
class ResidencePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidencePolicy
        fields = ('id', 'title', 'description', 'residence')

        extra_kwargs = {
            'residence': {'required': False, 'allow_null': True},
        }


class HotelPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPolicy
        fields = ('id', 'title', 'description', 'hotel')

        extra_kwargs = {
            'hotel': {'required': False, 'allow_null': True},
        }


# Price-related serializers---------------------------------------------------------------------------------------------
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['title']


class ResidencePriceInfoSerializer(serializers.ModelSerializer):
    # price = serializers.SerializerMethodField()

    class Meta:
        model = ResidencePriceInfo
        fields = ('id', 'currency', 'price', 'residence')
        extra_kwargs = {
            'residence': {'required': False, 'allow_null': True},
        }

    # def validate_price(self, attr):
    #     return attr*2
    # def get_price(self, obj: ResidencePriceInfo):
    #     return obj.get_price()


class UnitPriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitPriceInfo
        fields = ('id', 'currency', 'price', 'unit')
        extra_kwargs = {
            'unit': {'required': False, 'allow_null': True},
        }

    def price_calculator(self, obj):
        pass


# Image-related serializers---------------------------------------------------------------------------------------------
class ResidenceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResidenceImage
        fields = ('id', 'title', 'description', 'avatar', 'residence')
        extra_kwargs = {
            'residence': {'required': False, 'allow_null': True},
        }

class HotelImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelImage
        fields = ('id', 'title', 'description', 'avatar', 'hotel')
        extra_kwargs = {
            'hotel': {'required': False, 'allow_null': True},
        }


# Residences serializers------------------------------------------------------------------------------------------------
class UnitSerializer(serializers.ModelSerializer):
    facilities = UnitFacilitySerializer(many=True, read_only=True)
    price_info = UnitPriceInfoSerializer(many=False, read_only=True)

    class Meta:
        model = Unit
        fields = ('id', 'title', 'description', 'capacity', 'bedroom', 'bed', 'hotel',
                  'facilities', 'price_info')
        extra_kwargs = {'hotel': {'required': True, 'allow_null': True}}


class ResidenceSerializer(serializers.ModelSerializer):
    image_album = ResidenceImageSerializer(many=False, read_only=True)
    facilities = ResidenceFacilitySerializer(many=True, read_only=True)
    policies = ResidencePolicySerializer(many=True, read_only=True)
    price_info = ResidencePriceInfoSerializer(many=False, read_only=True)

    class Meta:
        model = Residence
        fields = ('id', 'title', 'description', 'capacity', 'bedroom', 'bed', 'city',
                  'image_album', 'facilities', 'policies', 'price_info')
        extra_kwargs = {'city': {'required': False, 'allow_null': True}}


class HotelSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    image_album = HotelImageSerializer(many=False, read_only=True)
    facilities = HotelFacilitySerializer(many=True, read_only=True)
    policies = HotelPolicySerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'units', 'city', 'image_album',
                  'facilities', 'policies')
        extra_kwargs = {'city': {'required': False, 'allow_null': True}}


# Location-related serializers------------------------------------------------------------------------------------------
class CitySerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True, read_only=True)
    residences = ResidenceSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'title', 'country', 'hotels', 'residences')
        extra_kwargs = {'country': {'required': False, 'allow_null': True}}


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'title', 'cities')

    # @staticmethod
    # def validate_title(attr):
    #     return attr.capitalize()


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

    @staticmethod
    def validate_date(attr):
        if attr < timezone.now().date():
            raise ValueError('Selected date is in the past')
        return attr


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

    @staticmethod
    def validate_date(attr):
        if attr < timezone.now().date():
            raise ValueError('Selected date is in the past')
        return attr

