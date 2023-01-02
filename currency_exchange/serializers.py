from rest_framework import serializers

class ExchangeSerializer(serializers.ModelSerializer):
    currency_to = serializers.CharField(max_length=3, required=True)
