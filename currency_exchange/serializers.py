from rest_framework import serializers

class ExchangeSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(max_length=3, required=True)
