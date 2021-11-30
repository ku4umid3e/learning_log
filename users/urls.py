"""Defines a URL schema for users"""

from django.urls import path, include

from . import views


app_name = 'users'
urlpatterns = [
            #Enable defaullt authorization URL.
            path('', include('django.contrib.auth.urls')),
            #Register page
            path('register/', views.register, name='register'),
]