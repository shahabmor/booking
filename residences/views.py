from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from permission.permission import UserPermission
from .serializers import *
from .models import *


# Location-related API ViewSets-----------------------------------------------------------------------------------------
class CountryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = City.objects.all()
    serializer_class = CitySerializer


# Residences API ViewSets-----------------------------------------------------------------------------------------------
class UnitViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class HotelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class ResidenceViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer


# Image_related API ViewSets--------------------------------------------------------------------------------------------
class ResidenceImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = ResidenceImage.objects.all()
    serializer_class = ResidenceImageSerializer


class HotelImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer


# Facility API ViewSet--------------------------------------------------------------------------------------------------
class ResidenceFacilityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = ResidenceFacility.objects.all()
    serializer_class = ResidenceFacilitySerializer


class HotelFacilityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = HotelFacility.objects.all()
    serializer_class = HotelFacilitySerializer

class UnitFacilityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = UnitFacility.objects.all()
    serializer_class = UnitFacilitySerializer


# Policy API ViewSet----------------------------------------------------------------------------------------------------
class ResidencePolicyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = ResidencePolicy.objects.all()
    serializer_class = ResidencePolicySerializer


class HotelPolicyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = HotelPolicy.objects.all()
    serializer_class = HotelPolicySerializer


# Price-related API ViewSet-----------------------------------------------------------------------------------------------------
class ResidencePriceInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = ResidencePriceInfo.objects.all()
    serializer_class = ResidencePriceInfoSerializer


class UnitPriceInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = UnitPriceInfo.objects.all()
    serializer_class = UnitPriceInfoSerializer


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
