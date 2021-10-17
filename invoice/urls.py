from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'invoice'

urlpatterns = [
    path('', InvoiceMainView.as_view(), name="invoice_main_view"),
    path('<int:id>', invoice_view, name="invoice_view"),
    path('print/<int:id>', invoice_print_view, name="invoice_print_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
