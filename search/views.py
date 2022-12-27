from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime

from .serializers import *
from tickets.models import AirplaneTicket
from residences.models import Residence, Hotel

now = timezone.localtime(timezone.now(), timezone.zoneinfo.ZoneInfo(key='Asia/Tehran'))

# AirPlane Ticket Search ViewSet---------------------------------------------------------------------------------------
class AirPlaneTicketSearchViewSet(GenericAPIView):
    serializer_class = AirPlaneTicketSearchSerializer

    def post(self, request):
        tickets = AirplaneTicket.valid_tickets.all()

        try:
            # origin check
            try:
                origin = request.data['origin']
                tickets = tickets.filter(origin__city__title=origin)
                if not tickets:
                    return Response('There is no flight from this city')
            except MultiValueDictKeyError:
                return Response('Origin field could not be empty')

            # destination check
            try:
                destination = request.data['destination']
                tickets = tickets.filter(destination__city__title=destination)
                if not tickets:
                    return Response('There is no flight to this city')
            except MultiValueDictKeyError:
                return Response('destination field could not be empty')

            # date check
            date = now.date()
            try:
                date = request.data['date']
            except MultiValueDictKeyError:
                pass
            finally:
                tickets = tickets.filter(time__gte=date)

            # count check
            count = 1
            try:
                count = request.data['count']
            except MultiValueDictKeyError:
                pass
            finally:
                tickets = tickets.filter(capacity__gte=count)
                if not tickets:
                    return Response(f'There is no airplane ticket with this credentials')

            # return result
            result = {}
            for ticket in tickets:
                price = ticket.price_info.first()
                info = {
                    "compony": ticket.company,
                    "origin": ticket.origin.city.title,
                    "destination": ticket.destination.city.title,
                    "date": ticket.time.date(),
                    "time": ticket.time.time(),
                    "capacity": ticket.capacity,
                    "price": str(price.price) + "-" + price.currency,
                }
                result[f'{ticket.id}'] = info

            return Response(result)

        except KeyError:
            return Response('origin, destination and date fields are empty')


# Residence Search ViewSet----------------------------------------------------------------------------------------------
class ResidenceSearchViewSet(GenericAPIView):
    serializer_class = ResidenceSearchSerializer

    def post(self, request):
        residences = Residence.objects.all()

        try:
            # city check
            try:
                city = request.data['city']
                residences = residences.filter(city__title=city)
                if not residences:
                    return Response('There is no Residence in this city')
            except MultiValueDictKeyError:
                return Response('City field could not be empty')

            # capacity check
            person = 1
            try:
                person = request.data['person']
            except MultiValueDictKeyError:
                pass
            finally:
                residences = residences.filter(capacity__gte=person)
                if not residences:
                    return Response(f'There is no residence with this credentials')

            # date check
            try:
                check_in = datetime.strptime(request.data['check_in'], '%Y-%m-%d')
                check_out = datetime.strptime(request.data['check_out'], '%Y-%m-%d')
                if check_in < now.now():
                    return Response('Check in date could not be in the past!')

                if check_out < check_in:
                    return Response('Check out date could not be before check in date!')

                date_check_result = []
                for residence in residences:
                    residence_is_full = False
                    for rented_day in residence.rented_days.all():
                        if check_in.date() <= rented_day.date <= check_out.date():
                            residence_is_full = True

                    if not residence_is_full:
                        date_check_result.append(residence)

                if not date_check_result:
                    return Response('There is no Residence in this time')
            except MultiValueDictKeyError:
                return Response('Date fields could not be empty')

            result = {}
            for residence in residences:
                price = residence.price_info.price
                currency = residence.price_info.currency

                info = {
                    "title": residence.title,
                    "capacity": residence.capacity,
                    "bedroom": residence.bedroom,
                    "bed": residence.bed,
                    "city": residence.city.title,
                    "price": str(price) + "-" + currency,
                }
                result[f'{residence.id}'] = info

            return Response(result)

        except KeyError:
            return Response('city, dates and number of people fields are empty')

