from django.urls import path
from .views import *


urlpatterns = [
    path('airplane_ticket/', AirPlaneTicketSearchViewSet.as_view()),
    path('residence/', ResidenceSearchViewSet.as_view()),
    path('hotel/', HotelSearchViewSet.as_view()),
]
