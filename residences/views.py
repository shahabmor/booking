from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .serializers import *
from .models import *


# Location-related API ViewSets-----------------------------------------------------------------------------------------
class CountryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Country.objects.filter(is_valid=True)
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class CityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = City.objects.filter(is_valid=True)
    serializer_class = CitySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Residences API ViewSets-----------------------------------------------------------------------------------------------
class UnitViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Unit.objects.filter(is_valid=True)
    serializer_class = UnitSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class HotelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Hotel.objects.filter(is_valid=True)
    serializer_class = HotelSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class ResidenceViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Residence.objects.filter(is_valid=True)
    serializer_class = ResidenceSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Image_related API ViewSets--------------------------------------------------------------------------------------------
class ImageAlbumViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = ImageAlbum.objects.filter(is_valid=True)
    serializer_class = ImageAlbumSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Image.objects.filter(is_valid=True)
    serializer_class = ImageSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Facility API ViewSet--------------------------------------------------------------------------------------------------
class FacilityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Facility.objects.filter(is_valid=True)
    serializer_class = FacilitySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Policy API ViewSet----------------------------------------------------------------------------------------------------
class PolicyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Policy.objects.filter(is_valid=True)
    serializer_class = PolicySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Price API ViewSet-----------------------------------------------------------------------------------------------------
class PriceInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = PriceInfo.objects.filter(is_valid=True)
    serializer_class = PriceInfoSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
