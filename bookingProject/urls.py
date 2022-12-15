from django.contrib import admin
from django.urls import path, include
import users.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(users.urls)),
]
