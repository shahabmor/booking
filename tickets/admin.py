from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Terminal)

admin.site.register(AirplaneTicket)

admin.site.register(AirPlaneTicketFacility)
admin.site.register(AirPlaneTicketPolicy)
admin.site.register(AirPlaneTicketPriceInfo)


