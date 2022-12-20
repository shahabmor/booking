from rest_framework import viewsets, parsers, renderers
from .serializers import *
from .models import *


# Location-related API ViewSets-----------------------------------------------------------------------------------------
class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.filter(is_valid=True)
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.filter(is_valid=True)
    serializer_class = CitySerializer


# Residences API ViewSets-----------------------------------------------------------------------------------------------
class UnitViewSet(viewsets.ModelViewSet):

    queryset = Unit.objects.filter(is_valid=True)
    serializer_class = UnitSerializer


class HotelViewSet(viewsets.ModelViewSet):

    queryset = Hotel.objects.filter(is_valid=True)
    serializer_class = HotelSerializer


class ResidenceViewSet(viewsets.ModelViewSet):

    queryset = Residence.objects.filter(is_valid=True)
    serializer_class = ResidenceSerializer


# Image_related API ViewSets--------------------------------------------------------------------------------------------
class ImageAlbumViewSet(viewsets.ModelViewSet):

    queryset = ImageAlbum.objects.filter(is_valid=True)
    serializer_class = ImageAlbumSerializer


class ImageViewSet(viewsets.ModelViewSet):

    queryset = Image.objects.filter(is_valid=True)
    serializer_class = ImageSerializer


# Facility API ViewSet--------------------------------------------------------------------------------------------------
class FacilityViewSet(viewsets.ModelViewSet):

    queryset = Facility.objects.filter(is_valid=True)
    serializer_class = FacilitySerializer


# Policy API ViewSet----------------------------------------------------------------------------------------------------
class PolicyViewSet(viewsets.ModelViewSet):

    queryset = Policy.objects.filter(is_valid=True)
    serializer_class = PolicySerializer


