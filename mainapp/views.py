from django.shortcuts import render, redirect

from django.http.response import HttpResponse
from . models import UserProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserForm
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password1']

            if UserProfile != None:
                user = authenticate(username=username, password=password)
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
            new_user = form.save()
            new_user = authenticate(username=new_user.username, password=form.cleaned_data["password1"])
            login(request, new_user)
            return redirect('home')
    form = UserForm
    content = {"form": form}
    return render(request, 'signup.html', content)
