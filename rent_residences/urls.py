from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *


urlpatterns = [
    path('country/', CountryAPIView.as_view()),
    path('city/', CityAPIView.as_view()),
    path('residence/', ResidencesAPIView.as_view()),
    path('hotel/', HotelsAPIView.as_view()),
]


