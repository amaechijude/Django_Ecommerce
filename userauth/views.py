from django.shortcuts import render, redirect
from django.conf import settings

from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import UserForm
from django.contrib import messages

import sys
sys.path.append('..')
from mainapp.views import home
 
# Create your views here.

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
