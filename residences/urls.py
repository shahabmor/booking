from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'residence', ResidenceViewSet, basename='residence')
router.register(r'hotels', HotelViewSet, basename='hotels')
router.register(r'units', UnitViewSet, basename='units')

router.register(r'images/residence', ResidenceImageViewSet, basename='images/residence')
router.register(r'images/hotel', HotelImageViewSet, basename='images/hotel')

router.register(r'facilities/residence', ResidenceFacilityViewSet, basename='facilities/residence')
router.register(r'facilities/hotel', HotelFacilityViewSet, basename='facilities/hotel')
router.register(r'facilities/unit', UnitFacilityViewSet, basename='facilities/unit')

router.register(r'policies/residence', ResidencePolicyViewSet, basename='policies/residence')
router.register(r'policies/hotel', HotelPolicyViewSet, basename='policies/hotel')

router.register(r'prices/residence', ResidencePriceInfoViewSet, basename='prices/residence')
router.register(r'prices/unit', UnitPriceInfoViewSet, basename='prices/unit')

router.register(r'rent/residence', viewset=RentResidenceViewSet, basename='rent/residence')
router.register(r'rent/hotel', viewset=RentHotelViewSet, basename='rent/hotel')


urlpatterns = []
urlpatterns += router.urls

