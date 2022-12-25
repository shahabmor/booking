
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, mixins
from permission.permission import UserPermission
from .serializers import *
from .models import *


# Location-related API ViewSets-----------------------------------------------------------------------------------------
class CountryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class CityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Residences API ViewSets-----------------------------------------------------------------------------------------------
class UnitViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class HotelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class ResidenceViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Image_related API ViewSets--------------------------------------------------------------------------------------------
class ImageAlbumViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = ImageAlbum.objects.all()
    serializer_class = ImageAlbumSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Facility API ViewSet--------------------------------------------------------------------------------------------------
class FacilityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Policy API ViewSet----------------------------------------------------------------------------------------------------
class PolicyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Price API ViewSet-----------------------------------------------------------------------------------------------------
class PriceInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = PriceInfo.objects.all()
    serializer_class = PriceInfoSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]


# Rent-related ViewSet--------------------------------------------------------------------------------------------------
class RentResidenceViewSet(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]

    queryset = RentResidence.objects.all()
    serializer_class = RentResidenceSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]

class RentHotelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = RentHotel.objects.all()
    serializer_class = RentHotelSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]





