from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'products'

urlpatterns = [
    path('', ProductsMainView.as_view(), name="products_main"),
    path('edit', edit_view, name="products_edit"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)

