from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, mixins
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


# Buy-related API ViewSet------------------------------------------------------------------------------------------------
class BuyAirPlaneTicketViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        if self.action == 'list':
            return AirplaneTicket.valid_tickets.all()
        return BuyAirPlaneTicket.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'list':
            return SeeAirplaneTicketSerializer
        return BuyAirPlaneTicketSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        count = data['count']
        ticket = AirplaneTicket.valid_tickets.get(id=data['ticket'])
        user = request.user

        if ticket.capacity > int(count):
            buy_airplane_ticket = BuyAirPlaneTicket.objects.create(user=user, ticket=ticket, count=count)
            buy_airplane_ticket.save()

            ticket.capacity -= int(count)
            ticket.save()

            serializer = BuyAirPlaneTicketSerializer(buy_airplane_ticket)
            return Response(serializer.data)

        raise ValueError(f'Only {ticket.capacity} tickets left!')


class SoldAirPlaneTicketViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = BuyAirPlaneTicket.objects.all()
    serializer_class = BuyAirPlaneTicketSerializer
