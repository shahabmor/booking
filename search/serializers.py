from rest_framework import serializers
from django.utils import timezone


# AirPlaneTicket Search Serializer-----------------------------------------------------------------------------------------------------
class AirPlaneTicketSearchSerializer(serializers.ModelSerializer):
    origin = serializers.CharField(max_length=50, allow_blank=True, required=False)
    destination = serializers.CharField(max_length=50, allow_blank=True, required=False)
    date = serializers.DateField(required=False, allow_null=True)
    person = serializers.IntegerField(default=1)


class ResidenceSearchSerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=50, allow_null=True, required=False)
    check_in = date = serializers.DateField(required=False, allow_null=True)
    check_out = serializers.DateField(required=False, allow_null=True)
    person = serializers.IntegerField(default=1)


