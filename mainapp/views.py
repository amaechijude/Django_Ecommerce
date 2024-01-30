from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.models import User
# Create your views here.

def signout(request):
    logout(request)
    messages.info(request, "You've loged out")
    return redirect('home')

def home(request, pk=0):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password1']
            
            user = authenticate(username=username, password=password)

            if user != None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "{Error: Couldn't sign in}")
                return redirect('home')
        return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return redirect('home')
        messages.info(request, "{Error: Could not sign up}")
        return redirect('signup')
    form = UserForm
    content = {"form": form}
    return render(request, 'signup.html', content)
