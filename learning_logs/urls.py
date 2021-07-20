'''Defines URL schemes for learning_logs'''

from django.urls import path
from . import views


urlpatterns = [
        #Home page
        path(r'', views.index, name='index'),
]
