from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'residence', ResidenceCommentViewSet, basename='residence')
router.register(r'hotel', HotelCommentViewSet, basename='hotel')
router.register(r'airplane_ticket', AirPlaneTicketCommentViewSet, basename='airplane_ticket')


router.register(r'rate/residence', ResidenceRatingViewSet, basename='rate/residence')
router.register(r'rate/hotel', HotelRatingViewSet, basename='rate/hotel')
router.register(r'rate/airplane_ticket', AirPlaneTicketRatingViewSet, basename='rate/airplane_ticket')


urlpatterns = []
urlpatterns += router.urls
