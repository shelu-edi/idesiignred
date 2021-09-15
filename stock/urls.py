from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'stock'

urlpatterns = [
    path('', stock_main_view, name="stock_view"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
