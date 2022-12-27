from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.utils import timezone

from .serializers import *
from tickets.models import AirplaneTicket

now = timezone.localtime(timezone.now(), timezone.zoneinfo.ZoneInfo(key='Asia/Tehran'))

# Search-related ViewSet------------------------------------------------------------------------------------------------
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
                info = {
                    "compony": ticket.company,
                    "origin": ticket.origin.city.title,
                    "destination": ticket.destination.city.title,
                    "date": ticket.time.date(),
                    "time": ticket.time.time(),
                    "capacity": ticket.capacity
                }
                result[f'{ticket.id}'] = info

            return Response(result)

        except KeyError:
            return Response('origin, destination and date fields are empty')
