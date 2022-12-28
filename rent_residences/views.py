from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .serializers import *
from residences.models import *

# Country APIView-------------------------------------------------------------------------------------------------------
class CountryAPIView(GenericAPIView):
    serializer_class = CountrySerializer

    def get(self, request):
        result = {}
        countries = Country.objects.all()

        for country in countries:
            result[f"{country.id}"] = country.title

        if result:
            return Response(result)

        return Response('No country has been defined.')

    def post(self, request):
        result = {}
        try:
            country_title = request.data['country']
            target_countries = Country.objects.filter(title__contains=country_title)
        except ObjectDoesNotExist:
            return Response(f'No country defined with this title')

        except KeyError:
            return Response('country title is required.')

        except MultipleObjectsReturned:
            return Response('country title could not be empty.')

        for country in target_countries:
            serialized_data = {}
            cities = country.cities.all()
            for city in cities:
                serialized_data[f"{city.id}"] = city.title
            result[f'{country.title}'] = serialized_data

        if result:
            return Response(result)
        return Response(f"No city has been defined here.")


# Country APIView-------------------------------------------------------------------------------------------------------
class CityAPIView(GenericAPIView):
    serializer_class = CitySerializer

    def get(self, request):
        result = {}
        cities = City.objects.all()

        for city in cities:
            result[f"{city.id}"] = city.title

        if result:
            return Response(result)

        return Response('No city has been defined.')

    def post(self, request):
        result = {}

        try:
            city_title = request.data['city']
            cities = City.objects.filter(title__contains=city_title)
        except ObjectDoesNotExist:
            return Response('No city has been defined with this title')

        except KeyError:
            return Response('city title is required.')

        except MultipleObjectsReturned:
            return Response('city title could not be empty.')

        for city in cities:
            serialized_data = {}

            residences = city.residences.all()
            hotels = city.hotels.all()

            serialized_residences = {}
            for residence in residences:
                serialized_residences[f"{residence.id}"] = residence.title

            serialized_hotels = {}
            for hotel in hotels:
                serialized_hotels[f"{hotel.id}"] = hotel.title

            serialized_data['residences'] = serialized_residences
            serialized_data['hotels'] = serialized_hotels

            result[f'{city.title}'] = serialized_data

        if result:
            return Response(result)

        return Response(f'No residence has been defined in {city_title}.')


# Residences APIView-----------------------------------------------------------------------------------------------------
class ResidencesAPIView(GenericAPIView):

    def get(self, request):
        result = {}
        residences = Residence.objects.all()

        for residence in residences:
            result[f"{residence.id}"] = {
                "title": residence.title,
                "city": residence.city.title,
            }
        if result:
            return Response(result)

        return Response('No residence has been defined.')

    def post(self, request):

        result = {}
        try:
            residence_title = request.data['residence']
            residences = Residence.objects.filter(title__contains=residence_title)
        except ObjectDoesNotExist:
            return Response('No residence has been defined with this title')

        except KeyError:
            return Response('residence title is required.')

        except MultipleObjectsReturned:
            return Response('residence title could not be empty.')

        for residence in residences:
            serialized_data = {}
            serialized_data['title'] = residence.title
            serialized_data['city'] = residence.city.title
            serialized_data['capacity'] = residence.capacity
            serialized_data['price'] = residence.price_info.price

            result[f'{residence.id}'] = serialized_data

        return Response(result)


# Hotel APIView-----------------------------------------------------------------------------------------------------
class HotelsAPIView(GenericAPIView):

    def get(self, request):
        result = {}
        hotels = Hotel.objects.all()

        for hotel in hotels:
            result[f"{hotel.id}"] = {
                "title": hotel.title,
                "city": hotel.city.title,
            }
        if result:
            return Response(result)

        return Response('No hotel has been defined.')

    def post(self, request):

        result = {}
        try:
            hotel_title = request.data['hotel']
            hotels = Hotel.objects.filter(title__contains=hotel_title)
        except ObjectDoesNotExist:
            return Response('No hotel has been defined with this title')

        except KeyError:
            return Response('hotel title is required.')

        except MultipleObjectsReturned:
            return Response('hotel title could not be empty.')

        for hotel in hotels:
            serialized_data = {}
            serialized_data['city'] = hotel.city.title

            serialized_units = {}
            for unit in hotel.units.all():
                serialized_units[f"{unit.title}"] = {
                    'capacity': unit.capacity,
                    'bedroom': unit.bedroom,
                    'bed': unit.bed,
                    'price': unit.price_info.price,
                }
            serialized_data['units'] = serialized_units

            result[f'{hotel.title}'] = serialized_data

        return Response(result)

