from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from permission.permission import UserPermission


from .models import *
from .serializers import *


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


# --------------------------------------------------rate----------------------------------------------------------------
# Residence Rating API Views--------------------------------------------------------------------------------------------
class ResidenceRatingViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = ResidenceRating.objects.all()
    serializer_class = ResidenceRatingSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]


# Hotel Rating API Views------------------------------------------------------------------------------------------------
class HotelRatingViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = HotelRating.objects.all()
    serializer_class = HotelRatingSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]


# Hotel Rating API Views------------------------------------------------------------------------------------------------
class AirPlaneTicketRatingViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = AirplaneTicketRating.objects.all()
    serializer_class = AirPlaneTicketRatingSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [UserPermission()]
