from rest_framework import viewsets, parsers, renderers
from .serializers import *
from .models import *


# Policy API ViewSet
class PolicyViewSet(viewsets.ModelViewSet):

    queryset = Policy.objects.filter(is_valid=True)
    serializer_class = PolicySerializer

    parser_classes = [parsers.JSONParser]
    renderer_classes = [renderers.JSONRenderer]


# Facility API ViewSet
class FacilityViewSet(viewsets.ModelViewSet):

    queryset = Facility.objects.filter(is_valid=True)
    serializer_class = FacilitySerializer

    parser_classes = [parsers.JSONParser]
    renderer_classes = [renderers.JSONRenderer]


# Image_related API ViewSets
class ImageAlbumViewSet(viewsets.ModelViewSet):

    queryset = ImageAlbum.objects.filter(is_valid=True)
    serializer_class = ImageAlbumSerializer

    parser_classes = [parsers.JSONParser, parsers.MultiPartParser]
    renderer_classes = [renderers.JSONRenderer, renderers.MultiPartRenderer]

class ImageViewSet(viewsets.ModelViewSet):

    queryset = Image.objects.filter(is_valid=True)
    serializer_class = ImageSerializer

    parser_classes = [parsers.JSONParser, parsers.MultiPartParser]
    renderer_classes = [renderers.JSONRenderer, renderers.MultiPartRenderer]


# Location-related API ViewSets
class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.filter(is_valid=True)
    serializer_class = CountrySerializer

    parser_classes = [parsers.JSONParser]
    renderer_classes = [renderers.JSONRenderer]

class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.filter(is_valid=True)
    serializer_class = CitySerializer

    parser_classes = [parsers.JSONParser]
    renderer_classes = [renderers.JSONRenderer]


# Unit API ViewSet
class UnitViewSet(viewsets.ModelViewSet):

    queryset = Unit.objects.filter(is_valid=True)
    serializer_class = UnitSerializer

    parser_classes = [parsers.JSONParser]
    renderer_classes = [renderers.JSONRenderer]

# Residences API ViewSets
class HotelViewSet(viewsets.ModelViewSet):

    queryset = Hotel.objects.filter(is_valid=True)
    serializer_class = HotelSerializer

    parser_classes = [parsers.JSONParser, parsers.MultiPartParser]
    renderer_classes = [renderers.JSONRenderer, renderers.MultiPartRenderer]


class ResidenceViewSet(viewsets.ModelViewSet):

    queryset = Residence.objects.filter(is_valid=True)
    serializer_class = ResidenceSerializer

    parser_classes = [parsers.JSONParser, parsers.MultiPartParser]
    renderer_classes = [renderers.JSONRenderer, renderers.MultiPartRenderer]
