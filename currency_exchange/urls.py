from django.urls import path
from .views import *


urlpatterns = [
    path('exchange/', ExchangeAPIView.as_view()),
]
