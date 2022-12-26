from .views import UserViewSet, LoginStepOneAPIView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, basename='')


urlpatterns = [
    path('login/', LoginStepOneAPIView.as_view(), name="step_one")
]
urlpatterns += router.urls
