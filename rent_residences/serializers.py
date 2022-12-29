from rest_framework import serializers


# Country Serializer----------------------------------------------------------------------------------------------------
class CountrySerializer(serializers.ModelSerializer):
    country = serializers.CharField(max_length=50, required=False, allow_null=True)


# City Serializer-------------------------------------------------------------------------------------------------------
class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=50)


# City Serializer-------------------------------------------------------------------------------------------------------
class ResidenceSerializer(serializers.ModelSerializer):
    residence = serializers.CharField(max_length=50)

# City Serializer-------------------------------------------------------------------------------------------------------
class HotelsSerializer(serializers.ModelSerializer):
    hotel = serializers.CharField(max_length=50)


