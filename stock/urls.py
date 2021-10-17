from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'stock'

urlpatterns = [
    path('', stock_main_view, name="stock-main"),

    # url(r'^/create/$', stock_create_view, name='stock-create'),
    path('/create/', stock_create_view, name='stock-create'),
    url(r'^stock/(?P<pk>\d+)/update/$', stock_update_view, name='stock-update')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)

