from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'residence', ResidenceViewSet, basename='residence')
router.register(r'hotels', HotelViewSet, basename='hotels')
router.register(r'units', UnitViewSet, basename='units')
router.register(r'images', ImageViewSet, basename='images')
router.register(r'image_album', ImageAlbumViewSet, basename='image_album')
router.register(r'facilities', FacilityViewSet, basename='facilities')
router.register(r'policies', PolicyViewSet, basename='policies')


urlpatterns = []
urlpatterns += router.urls

