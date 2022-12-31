from rest_framework import serializers
from tickets.models import *


# Facility serializer---------------------------------------------------------------------------------------------------
class AirPlaneTicketFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirPlaneTicketFacility
        fields = ('id', 'title', 'description', 'airplane_ticket')
        extra_kwargs = {
            'airplane_ticket': {'required': False, 'allow_null': True},
        }


# Policy serializer-----------------------------------------------------------------------------------------------------
class AirPlaneTicketPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirPlaneTicketPolicy
        fields = ('id', 'title', 'description', 'airplane_ticket')
        extra_kwargs = {
            'airplane_ticket': {'required': False, 'allow_null': True},
        }


# Price_info serializer-------------------------------------------------------------------------------------------------
class AirPlaneTicketPriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirPlaneTicketPriceInfo
        fields = ('id', 'currency', 'price', 'airplane_ticket')
        extra_kwargs = {
            'airplane_ticket': {'required': False, 'allow_null': True},
        }


# Ticket serializer-----------------------------------------------------------------------------------------------------
class AirplaneTicketSerializer(serializers.ModelSerializer):
    facilities = AirPlaneTicketFacilitySerializer(many=True, read_only=True)
    policies = AirPlaneTicketPolicySerializer(many=True, read_only=True)
    price_info = AirPlaneTicketPriceInfoSerializer(many=False, read_only=True)

    class Meta:
        model = AirplaneTicket
        fields = ('id', 'company', 'description', 'origin', 'destination', 'time', 'duration',
                  'airplane', 'flight_number', 'terminal', 'capacity', 'facilities', 'policies', 'price_info')


# Terminal-related serializers------------------------------------------------------------------------------------------
class TerminalSerializer(serializers.ModelSerializer):
    airplanetickets_departure = AirplaneTicketSerializer(many=True, read_only=True)
    airplanetickets_arrival = AirplaneTicketSerializer(many=True, read_only=True)

    class Meta:
        model = Terminal
        fields = ('id', 'title', 'description', 'city', 'airplanetickets_departure', 'airplanetickets_arrival')
        extra_kwargs = {'city': {'required': False, 'allow_null': True}}


class CitySerializer(serializers.ModelSerializer):
    terminals = TerminalSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'title', 'country', 'terminals')
        extra_kwargs = {'country': {'required': False, 'allow_null': True}}


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'title', 'cities')


# Buy-related Serializers-----------------------------------------------------------------------------------------------
class SeeAirplaneTicketSerializer(serializers.ModelSerializer):

    facilities = AirPlaneTicketFacilitySerializer(many=True, read_only=True)
    policies = AirPlaneTicketPolicySerializer(many=True, read_only=True)
    price_info = AirPlaneTicketPriceInfoSerializer(many=False, read_only=True)

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


