from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'residence', ResidenceCommentViewSet, basename='residence')
router.register(r'hotel', HotelCommentViewSet, basename='hotel')
router.register(r'airplane_ticket', AirPlaneTicketCommentViewSet, basename='airplane_ticket')


urlpatterns = []
urlpatterns += router.urls
