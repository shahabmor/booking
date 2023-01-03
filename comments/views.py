from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from permission.permission import UserPermission

from .models import ResidenceComment, HotelComment, AirplaneTicketComment
from .serializers import ResidenceCommentSerializer, HotelCommentSerializer, AirPlaneTicketCommentSerializer


# Residence Comment API Views-------------------------------------------------------------------------------------------
class ResidenceCommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = ResidenceComment.objects.all()
    serializer_class = ResidenceCommentSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]


# Hotel API Views-------------------------------------------------------------------------------------------------------
class HotelCommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = HotelComment.objects.all()
    serializer_class = HotelCommentSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]


# AirPlane Ticket Comment API Views-------------------------------------------------------------------------------------
class AirPlaneTicketCommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = AirplaneTicketComment.objects.all()
    serializer_class = AirPlaneTicketCommentSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]
