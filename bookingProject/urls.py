from django.contrib import admin
# from django_restful_admin import admin
from django.urls import path, include
import users.urls
import residences.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(residences.urls)),
    path('', include(users.urls)),


]
