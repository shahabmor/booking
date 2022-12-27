from django.urls import path
from .views import *


urlpatterns = [
    path('airplane_ticket/', AirPlaneTicketSearchViewSet.as_view()),
]
