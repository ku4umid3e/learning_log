"""Defines URL schemes for learning_logs"""

from django.urls import path, re_path
from . import views

app_name = 'learning_logs'
urlpatterns = [
        # Home page
        path('', views.index, name='index'),
        # Output all topics.
        re_path(r'^topics/$', views.topics, name='topics'),
        # Page with detailed information on a separate topic.
        re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        # Page to add a new topic.
        re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
        # Page to add a new entry.
        re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
        # Page to edit entry
        re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
