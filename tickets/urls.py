from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'terminals', TerminalViewSet, basename='terminals')
router.register(r'airplane', AirplaneTicketViewSet, basename='airplane')
router.register(r'facilities', FacilityViewSet, basename='facilities')
router.register(r'policies', PolicyViewSet, basename='policies')
router.register(r'prices', PriceInfoViewSet, basename='prices')
router.register(r'buy/airplane', BuyAirPlaneTicketViewSet, basename='buy/airplane')
router.register(r'sold/airplane', SoldAirPlaneTicketViewSet, basename='sold/airplane')

urlpatterns = []
urlpatterns += router.urls
