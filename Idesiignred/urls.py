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
    path('customer/', include('customers.urls')),
    path('users/', include('users.urls')),

    path('super-admin-dashboard', super_admin_dashboard_view, name='super-admin-dashboard'),

    path('ladies-frock-sample-profit', ladies_frock_profit_view, name='ladies-frock-sample-product-view'),
    path('ladies-frock-accepted', ladies_frock_sample_accept_view, name='ladies-frock-accepted'),

    path('ladies-blouse-sample-profit', ladies_blouse_profit_view, name='ladies-blouse-sample-product-view'),
    path('ladies-blouse-accepted', ladies_blouse_sample_accept_view, name='ladies-blouse-accepted'),

    path('ladies-skirt-sample-profit', ladies_skirt_profit_view, name='ladies-skirt-sample-product-view'),
    path('ladies-skirt-accepted', ladies_skirt_sample_accept_view, name='ladies-skirt-accepted'),

    path('ladies-pant-sample-profit', ladies_pant_profit_view, name='ladies-pant-sample-product-view'),
    path('ladies-pant-accepted', ladies_pant_sample_accept_view, name='ladies-pant-accepted'),

    path('ladies-tshirt-sample-profit', ladies_tshirt_profit_view, name='ladies-tshirt-sample-product-view'),
    path('ladies-tshirt-accepted', ladies_tshirt_sample_accept_view, name='ladies-tshirt-accepted'),

    path('maternity-frock-sample-profit', ladies_maternity_frock_profit_view, name='maternity-frock-sample-product-view'),
    path('maternity-frock-accepted', ladies_maternity_frock_sample_accept_view, name='maternity-frock-accepted'),

    path('kaftan-sample-profit', kaftan_profit_view, name='kaftan-sample-product-view'),
    path('kaftan-accepted', kaftan_sample_accept_view, name='kaftan-accepted'),

    path('nigtwear-sample-profit', nightwear_profit_view, name='nightwear-sample-product-view'),
    path('nightwear-accepted', nightwear_sample_accept_view, name='nightwear-frock-accepted'),

    path('order-price', order_order_price_view, name='order-price'),
    path('order-completed', order_completed_view, name='order-completed'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
