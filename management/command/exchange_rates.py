from django.core.management import BaseCommand
from residences.models import CurrencyExchangeRate
from utils.redis.connection import get_redis_client

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         exchange_rates = CurrencyExchangeRate.objects.all()
#         redis_client = get_redis_client()
#
#         mapping = {}
#         for exchange_rate in exchange_rates:
#             mapping = {f'{exchange_rate.currency_from}/{exchange_rate.currency_to}': exchange_rate.rate}
#
#         redis_client.hset('currency_exchange_rates', mapping=mapping)
