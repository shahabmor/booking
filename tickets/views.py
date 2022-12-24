from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .serializers import *
from .models import *


# Ticket API ViewSet--------------------------------------------------------------------------------------------------
class AirplaneTicketViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = AirplaneTicket.objects.all()
    serializer_class = AirplaneTicketSerializer


# Terminal-related API ViewSets-----------------------------------------------------------------------------------------
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


class TerminalViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


# Facility API ViewSet--------------------------------------------------------------------------------------------------
class FacilityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


# Policy API ViewSet----------------------------------------------------------------------------------------------------
class PolicyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


# Price API ViewSet-----------------------------------------------------------------------------------------------------
class PriceInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = PriceInfo.objects.all()
    serializer_class = PriceInfoSerializer

