from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """Home page of the Learning Log application"""
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
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a specific topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #No data was sent; an empty forms created
        form = EntryForm()

    else:
        #POST data has been sent; process the data.
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic' : topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
    
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #Original request; the form is filled with the data of the current record.
        form = EntryForm(instance=entry)
    else:
        #POST data has been sent; process the data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
