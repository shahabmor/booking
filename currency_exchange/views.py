from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from residences.models import CurrencyExchangeRate, ResidencePriceInfo, UnitPriceInfo, Currency
from tickets.models import AirPlaneTicketPriceInfo


# Exchange API----------------------------------------------------------------------------------------------------------
class ExchangeAPIView(GenericAPIView):

    def post(self, request):
        currencies = Currency.objects.all()
        currency_exchange_rates = CurrencyExchangeRate.objects.all()
        residences_price = ResidencePriceInfo.objects.all()
        units_price = UnitPriceInfo.objects.all()
        airplane_tickets_price = AirPlaneTicketPriceInfo.objects.all()

        try:
            currency_to = request.data['currency'].upper()
        except KeyError:
            return Response('currency_to field is required')

        valid_currency = False
        for currency in currencies:
            if currency.title == currency_to:
                valid_currency = True

        if not valid_currency:
            return Response('currency in not valid')

        # residence price
        for residence_price in residences_price:
            currency_from = residence_price.currency.title

            for exchange_rate in currency_exchange_rates:
                if exchange_rate.currency_from.title == currency_from and exchange_rate.currency_to.title == currency_to:
                    residence_price.price = residence_price.price * exchange_rate.rate
                    residence_price.currency = exchange_rate.currency_to
                    residence_price.save()

        # unit price
        for unit_price in units_price:
            currency_from = unit_price.currency.title

            for exchange_rate in currency_exchange_rates:
                if exchange_rate.currency_from.title == currency_from and exchange_rate.currency_to.title == currency_to:
                    unit_price.price = unit_price.price * exchange_rate.rate
                    unit_price.currency = exchange_rate.currency_to
                    unit_price.save()

        # airplane ticket price
        for airplane_ticket_price in airplane_tickets_price:
            currency_from = airplane_ticket_price.currency.title

            for exchange_rate in currency_exchange_rates:
                if exchange_rate.currency_from.title == currency_from and exchange_rate.currency_to.title == currency_to:
                    airplane_ticket_price.price = airplane_ticket_price.price * exchange_rate.rate
                    airplane_ticket_price.currency = exchange_rate.currency_to
                    airplane_ticket_price.save()

        return Response(f'Exchange prices to: {currency_to}')
