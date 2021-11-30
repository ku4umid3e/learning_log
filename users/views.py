from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Registers a new user"""
    if request.method != 'POST':
        #Displays an empty registration form.
        form = UserCreationForm()
    else:
        #Processing filled form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Entry and redirection to the homepage.
            login(request, new_user)
            return redirect('learning_logs:index')
    #
    context = {'form': form}
    return render(request, 'users/register.html', context)
