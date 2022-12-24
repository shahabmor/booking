from django.contrib import admin
# from django_restful_admin import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import users.urls
import residences.urls
import tickets.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(residences.urls)),
    path('', include(users.urls)),
    path('tickets/', include(tickets.urls)),

    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
