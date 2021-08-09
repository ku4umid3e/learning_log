from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForms

# Create your views here.
def index(request):
    """Home page of the Lerning Log application"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Displays a list of topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Display one topic and all its records."""
    topic = Topic.objects.get(id=topic_id)
    entries =  topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Determines a new topic."""
    if request.method != 'POST':
        # The data was not sent; Created empty form.
        form =TopicForm()
    else:
        # POST data sent; process data.
        from = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)
