from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils import timezone
from datetime import datetime

from .serializers import *
from tickets.models import AirplaneTicket
from residences.models import Residence, Hotel, Unit

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
                tickets = tickets.filter(origin__city__title__contains=origin)
                if not tickets:
                    return Response('There is no flight from this city')
            except MultiValueDictKeyError:
                return Response('Origin field could not be empty')

            # destination check
            try:
                destination = request.data['destination']
                tickets = tickets.filter(destination__city__title__contains=destination)
                if not tickets:
                    return Response('There is no flight to this city')
            except MultiValueDictKeyError:
                return Response('destination field could not be empty')

            # date check
            date = now.date()
            try:
                date = request.data['date']
                tickets = tickets.filter(time__gte=date)

            except ValidationError:
                return Response("value has an invalid format. It must be in YYYY-MM-DD format")

            # count check
            try:
                person = request.data['person']
                tickets = tickets.filter(capacity__gte=person)
                if not tickets:
                    return Response(f'There is no airplane ticket with this credentials')
            except ValueError:
                return Response(f'person field accept integer number')

            # return result
            result = {}
            for ticket in tickets:
                try:
                    price = ticket.price_info
                    amount = str(price.price)
                    currency = price.currency.title

                except ObjectDoesNotExist:
                    amount = '--'
                    currency = '--'

                info = {
                    "compony": ticket.company,
                    "origin": ticket.origin.city.title,
                    "destination": ticket.destination.city.title,
                    "date": ticket.time.date(),
                    "time": ticket.time.time(),
                    "capacity": ticket.capacity,
                    "price": amount + "-" + currency,
                }
                result[f'{ticket.id}'] = info

                comments = ticket.comments.all()
                serialized_comments = {}
                for comment in comments:
                    if not comment.parent:
                        serialized_comments[f"id:{comment.id}/ usr:{comment.user.username}"] = comment.comment_body
                    else:
                        serialized_comments[
                            f"id:{comment.id}/ usr:{comment.user.username} (reply-to:{comment.parent.id})"] \
                            = comment.comment_body

                result['comments'] = serialized_comments

                # rate section
                result['rate'] = ticket.average_rating

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
                residences = residences.filter(city__title__contains=city)
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
                return Response('check_in and check_out fields are required')

            result = {}
            for residence in residences:

                try:
                    price = residence.price_info
                    currency = price.currency.title
                    price_per_day = {}

                    go_on = True
                    date = check_in
                    day_number = 1
                    while go_on:
                        amount = str(price.get_price(date=date))
                        price_per_day[f'{date}'] = amount + '-' + currency

                        date += timezone.timedelta(days=1)
                        day_number += 1
                        if date > check_out:
                            go_on = False

                except ObjectDoesNotExist:
                    price_per_day = 'not defined'

                info = {
                    "title": residence.title,
                    "capacity": residence.capacity,
                    "bedroom": residence.bedroom,
                    "bed": residence.bed,
                    "city": residence.city.title,
                    "price": price_per_day,
                }

                comments = residence.comments.all()
                serialized_comments = {}
                for comment in comments:
                    if not comment.parent:
                        serialized_comments[f"id:{comment.id}/ usr:{comment.user.username}"] = comment.comment_body
                    else:
                        serialized_comments[
                            f"id:{comment.id}/ usr:{comment.user.username} (reply-to:{comment.parent.id})"] \
                            = comment.comment_body

                info['comments'] = serialized_comments

                # rate section
                info['rate'] = residence.average_rating

                result[f'{residence.id}'] = info

            if result:
                return Response(result)
            return Response('There is no available residence with these credentials')

        except KeyError:
            return Response('city, dates and number of people fields are empty')


# Hotel Search ViewSet----------------------------------------------------------------------------------------------
class HotelSearchViewSet(GenericAPIView):
    serializer_class = ResidenceSearchSerializer

    def post(self, request):
        units = Unit.objects.all()

        try:
            # city check
            try:
                city = request.data['city']
                units = units.filter(hotel__city__title__contains=city)
                if not units:
                    return Response('There is no Hotel in this city')
            except MultiValueDictKeyError:
                return Response('City field could not be empty')

            # date check
            try:
                check_in = datetime.strptime(request.data['check_in'], '%Y-%m-%d')
                check_out = datetime.strptime(request.data['check_out'], '%Y-%m-%d')
                if check_in < now.now():
                    return Response('Check in date could not be in the past!')

                if check_out < check_in:
                    return Response('Check out date could not be before check in date!')

                date_check_result = []
                for unit in units:
                    unit_is_full = False
                    for rented_day in unit.rented_days.all():
                        if check_in.date() <= rented_day.date <= check_out.date():
                            unit_is_full = True

                    if not unit_is_full:
                        date_check_result.append(unit)

                if not date_check_result:
                    return Response('There is no available hotel in this time')
            except MultiValueDictKeyError:
                return Response('check_in and check_out fields are required')

            # hotel info serializer
            hotel_result = {}
            for unit in date_check_result:
                hotel_result[f'{unit.hotel.title}'] = None

            for hotel in hotel_result:
                hotel_info = {}
                units_info = {}
                hotel_capacity = 0
                for unit in date_check_result:
                    if unit.hotel.title == hotel:
                        try:
                            price = unit.price_info
                            currency = price.currency.title
                            price_per_day = {}

                            go_on = True
                            date = check_in
                            day_number = 1
                            while go_on:
                                amount = str(price.get_price(date=date))
                                price_per_day[f'{date}'] = amount + '-' + currency

                                date += timezone.timedelta(days=1)
                                day_number += 1
                                if date > check_out:
                                    go_on = False

                        except ObjectDoesNotExist:
                            price_per_day = 'not defined'

                        unit_info = {
                            'id': unit.pk,
                            'capacity': unit.capacity,
                            'bedroom': unit.bedroom,
                            'bed': unit.bed,
                            'price_info': price_per_day,
                        }
                        units_info[f'room {unit.title}'] = unit_info
                        hotel_capacity += unit.capacity

                hotel_info['units'] = units_info
                hotel_info['available_capacity'] = hotel_capacity

                # comment section
                target_hotel = Hotel.objects.get(title=hotel)
                comments = target_hotel.comments.all()
                serialized_comments = {}
                for comment in comments:
                    if not comment.parent:
                        serialized_comments[f"id:{comment.id}/ usr:{comment.user.username}"] = comment.comment_body
                    else:
                        serialized_comments[
                            f"id:{comment.id}/ usr:{comment.user.username} (reply-to:{comment.parent.id})"] \
                            = comment.comment_body

                hotel_info['comments'] = serialized_comments

                # rate section
                hotel_info['rate'] = target_hotel.average_rating

                hotel_result[hotel] = hotel_info
            # capacity check
            capacity_check_result = []
            person = 1
            try:
                person = request.data['person']
            except MultiValueDictKeyError:
                pass
            finally:
                for hotel in hotel_result:
                    if hotel_result[hotel]['available_capacity'] >= int(person):
                        capacity_check_result.append(hotel)

            # serializing the result data
            result = {}
            for hotel_title in capacity_check_result:
                result[f'{hotel_title}'] = hotel_result[f'{hotel_title}']

            if result:
                return Response(result)
            return Response('There is no available hotel with these credentials')

        except KeyError:
            return Response('city, dates and number of people fields are empty')



