
from django.contrib import admin
from django.urls import path, include

import crudapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crudapp.urls')),
]
