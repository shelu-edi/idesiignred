from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'users'

urlpatterns = [
    url(r'^logout/$', logout_view, name='user-logout'),
    path('login', UserLoginView.as_view(), name="user_login_view"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
