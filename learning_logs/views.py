from django.shortcuts import render

# Create your views here.
def index(request):
    """Home page of the Lerning Log application"""
    return render(request, 'learning_logs/index.html')
