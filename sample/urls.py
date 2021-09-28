from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'sample'

urlpatterns = [
    path('', SampleMainView.as_view(), name="sample_view"),

    # ladies
    path('ladies-frock/<int:id>/', ladies_frock_view, name="ladies_frock_view"),
    path('ladies-blouse/<int:id>/', ladies_blouse_view, name="ladies_blouse_view"),
    path('ladies-pant/<int:id>/', ladies_pant_view, name="ladies_pant_view"),
    path('ladies-skirt/<int:id>/', ladies_skirt_view, name="ladies_skirt_view"),
    path('ladies-tshirt/<int:id>/', ladies_tshirt_view, name="ladies_tshirt_view"),
    path('maternity-frock/<int:id>/', maternity_frock_view, name="maternity_frock_view"),
    path('kaftan/<int:id>/', kaftan_view, name="kaftan_view"),
    path('nightwear/<int:id>/', nightwear_view, name="nightwear_view"),

    path('ladies-frock/print/<int:id>/', ladies_frock_print_view, name="ladies_frock_print_view"),
    path('ladies-blouse/print/<int:id>/', ladies_blouse_print_view, name="ladies_blouse_print_view"),
    path('ladies-pant/print/<int:id>/', ladies_pant_print_view, name="ladies_pant_print_view"),
    path('ladies-skirt/print/<int:id>/', ladies_skirt_print_view, name="ladies_skirt_print_view"),
    path('ladies-tshirt/print/<int:id>/', ladies_tshirt_print_view, name="ladies_tshirt_print_view"),
    path('maternity-frock/print/<int:id>/', maternity_frock_print_view, name="maternity_frock_print_view"),
    path('kaftan/print/<int:id>/', kaftan_print_view, name="kaftan_print_view"),
    path('nightwear/print/<int:id>/', nightwear_print_view, name="nightwear_print_view"),

    # boys
    path('boys-pant/<int:id>/', boys_pant_view, name="boys_pant_view"),
    path('boys-shirt/<int:id>/', boys_shirt_view, name="boys_shirt_view"),
    path('boys-tshirt/<int:id>/', boys_tshirt_view, name="boys_tshirt_view"),
    path('boys-short/<int:id>/', boys_short_view, name="boys_short_view"),

    path('boys-pant/print/<int:id>/', boys_pant_print_view, name="boys_pant_print_view"),
    path('boys-shirt/print/<int:id>/', boys_shirt_print_view, name="boys_shirt_print_view"),
    path('boys-tshirt/print/<int:id>/', boys_tshirt_print_view, name="boys_tshirt_print_view"),
    path('boys-short/print/<int:id>/', boys_short_print_view, name="boys_short_print_view"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
