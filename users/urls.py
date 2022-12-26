from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, basename='')


urlpatterns = [
    path('login/step_one/', LoginStepOneAPIView.as_view(), name="step_one"),
    path('login/step_two/', LoginStepTwoAPIView.as_view(), name="step_two")
]
urlpatterns += router.urls
