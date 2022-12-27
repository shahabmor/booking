from rest_framework import serializers
from django.utils import timezone


# AirPlaneTicket Search Serializer-----------------------------------------------------------------------------------------------------
class AirPlaneTicketSearchSerializer(serializers.ModelSerializer):
    origin = serializers.CharField(max_length=50, allow_blank=True, required=False)
    destination = serializers.CharField(max_length=50, allow_blank=True, required=False)
    date = serializers.DateField(required=False, allow_null=True)
    count = serializers.IntegerField(default=1)
