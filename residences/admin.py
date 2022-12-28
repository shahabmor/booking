from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(City)

admin.site.register(Unit)
admin.site.register(Hotel)
admin.site.register(Residence)

admin.site.register(ResidenceImage)
admin.site.register(HotelImage)

admin.site.register(ResidencePriceInfo)
admin.site.register(UnitPriceInfo)

admin.site.register(ResidencePolicy)
admin.site.register(HotelPolicy)

admin.site.register(ResidenceFacility)
admin.site.register(HotelFacility)
admin.site.register(UnitFacility)

