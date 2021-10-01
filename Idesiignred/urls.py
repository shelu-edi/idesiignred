"""Idesiignred URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from pages.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('search_results/', search_results, name="search-results"),

    path('orders/', include('orders.urls')),
    path('fabric/', include('fabric.urls')),
    path('cutting/', include('cutting.urls')),
    path('accessories/', include('accessories.urls')),
    path('sewing/', include('sewing.urls')),
    path('stock/', include('stock.urls')),
    path('invoice/', include('invoice.urls')),
    path('sample/', include('sample.urls')),
    path('product/', include('products.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
