'''Defines URL schemes for learning_logs'''

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
        # Home page
        path('', views.index, name='index'),
        # Output all topics.
        path('topics', views.topics, name='topics'),
        # Page with detailed information on a separate topic.
        path(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'),
]
