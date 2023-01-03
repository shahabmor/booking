from django.contrib import admin
from .models import *

admin.site.register(ResidenceComment)
admin.site.register(HotelComment)
admin.site.register(AirplaneTicketComment)

admin.site.register(ResidenceRating)
admin.site.register(HotelRating)
admin.site.register(AirplaneTicketRating)
