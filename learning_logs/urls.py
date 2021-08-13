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
        path('topic', views.topic, name='topic'),
        # Page to add a new topic.
        path('new_topic', views.new_topic, name='new_topic'),
]
