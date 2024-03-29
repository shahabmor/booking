from django.contrib import admin
# from django_restful_admin import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import users.urls
import residences.urls
import rent_residences.urls
import tickets.urls
import search.urls
import currency_exchange.urls
import comments.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('residences/', include(residences.urls)),
    path('rent/', include(rent_residences.urls)),
    path('users/', include(users.urls)),
    path('tickets/', include(tickets.urls)),
    path('search/', include(search.urls)),
    path('currency/', include(currency_exchange.urls)),
    path('comment/', include(comments.urls)),

    # path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
