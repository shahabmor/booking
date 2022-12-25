from rest_framework import serializers
from tickets.models import *


# Facility serializer---------------------------------------------------------------------------------------------------
class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('id', 'title', 'description', 'airplane_ticket',
                  'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {
            'airplane_ticket': {'required': False, 'allow_null': True},
        }


# Policy serializer-----------------------------------------------------------------------------------------------------
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ('id', 'title', 'description', 'airplane_ticket',
                  'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {
            'airplane_ticket': {'required': False, 'allow_null': True},
        }


# Price_info serializer-------------------------------------------------------------------------------------------------
class PriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceInfo
        fields = ('id', 'currency', 'price', 'airplane_ticket',
                  'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {
            'airplane_ticket': {'required': False, 'allow_null': True},
        }


# Ticket serializer-----------------------------------------------------------------------------------------------------
class AirplaneTicketSerializer(serializers.ModelSerializer):
    facilities = FacilitySerializer(many=True, read_only=True)
    policies = PolicySerializer(many=True, read_only=True)
    price_info = PriceInfoSerializer(many=False, read_only=True)

    class Meta:
        model = AirplaneTicket
        fields = ('id', 'company', 'description', 'origin', 'destination', 'time', 'duration',
                  'airplane', 'flight_number', 'terminal', 'capacity', 'facilities', 'policies', 'price_info',
                  'is_valid', 'created_time', 'modified_time')


# Terminal-related serializers------------------------------------------------------------------------------------------
class TerminalSerializer(serializers.ModelSerializer):
    airplanetickets_departure = AirplaneTicketSerializer(many=True, read_only=True)
    airplanetickets_arrival = AirplaneTicketSerializer(many=True, read_only=True)

    class Meta:
        model = Terminal
        fields = ('id', 'title', 'description', 'city', 'airplanetickets_departure', 'airplanetickets_arrival',
                  'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {'city': {'required': False, 'allow_null': True}}


class CitySerializer(serializers.ModelSerializer):
    terminals = TerminalSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'title', 'country', 'terminals', 'is_valid', 'created_time', 'modified_time')
        extra_kwargs = {'country': {'required': False, 'allow_null': True}}


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'title', 'is_valid', 'cities', 'created_time', 'modified_time')


# Buy-related Serializers-----------------------------------------------------------------------------------------------
class SeeAirplaneTicketSerializer(serializers.ModelSerializer):

    facilities = FacilitySerializer(many=True, read_only=True)
    policies = PolicySerializer(many=True, read_only=True)
    price_info = PriceInfoSerializer(many=False, read_only=True)

    class Meta:
        model = AirplaneTicket
        fields = ('id', 'company', 'description', 'origin', 'destination', 'time', 'duration',
                  'airplane', 'flight_number', 'terminal', 'capacity', 'facilities', 'policies', 'price_info')


class BuyAirPlaneTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyAirPlaneTicket
        fields = ('id', 'user', 'ticket', 'count')
        extra_kwargs = {'ticket': {'allow_null': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(BuyAirPlaneTicketSerializer, self).create(validated_data)


# Search Serializer-----------------------------------------------------------------------------------------------------
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneTicket
        fields = ('company', 'time', 'origin', 'destination')

