from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'fabric'

urlpatterns = [
    path('', fabric_main_view, name="fabric_view"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
