from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, mixins
from permission.permission import UserPermission
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
class AirPlaneTicketFacilityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = AirPlaneTicketFacility.objects.all()
    serializer_class = AirPlaneTicketFacilitySerializer


# Policy API ViewSet----------------------------------------------------------------------------------------------------
class AirPlaneTicketPolicyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = AirPlaneTicketPolicy.objects.all()
    serializer_class = AirPlaneTicketPolicySerializer


# Price API ViewSet-----------------------------------------------------------------------------------------------------
class AirPlaneTicketPriceInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = AirPlaneTicketPriceInfo.objects.all()
    serializer_class = AirPlaneTicketPriceInfoSerializer


# Buy-related API ViewSet------------------------------------------------------------------------------------------------
class BuyAirPlaneTicketViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        if self.action == 'list':
            return AirplaneTicket.valid_tickets.all()
        return BuyAirPlaneTicket.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [UserPermission()]

    def get_serializer_class(self):
        if self.action == 'list':
            return SeeAirplaneTicketSerializer
        return BuyAirPlaneTicketSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            count = data['count']
            try:
                ticket = AirplaneTicket.valid_tickets.get(id=data['ticket'])
            except ObjectDoesNotExist:
                return Response(f'there is no flight with this id')
            user = request.user

        except KeyError:
            return Response('ticket and count fields are required')

        if ticket.capacity >= int(count):
            buy_airplane_ticket = BuyAirPlaneTicket.objects.create(user=user, ticket=ticket, count=count)
            buy_airplane_ticket.save()

            ticket.capacity -= int(count)
            ticket.save()

            serializer = BuyAirPlaneTicketSerializer(buy_airplane_ticket)
            return Response(serializer.data)

        return Response(f'Only {ticket.capacity} tickets left!')


class SoldAirPlaneTicketViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = BuyAirPlaneTicket.objects.all()
    serializer_class = BuyAirPlaneTicketSerializer



