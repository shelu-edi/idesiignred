from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'sample'

urlpatterns = [
    path('', SampleMainView.as_view(), name="sample_view"),

    path('ladies-frock/<int:id>/', ladies_frock_view, name="ladies_frock_view"),
    path('ladies-blouse/<int:id>/', ladies_blouse_view, name="ladies_blouse_view"),

    path('ladies-frock/print/<int:id>/', ladies_frock_print_view, name="ladies_frock_print_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
