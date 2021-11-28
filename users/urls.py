"""Defines a URL schema for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
            #Enable defaullt authorization URL.
            path('', include('django.contrib.auth.urls')),
]