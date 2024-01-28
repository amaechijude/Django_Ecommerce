from django.shortcuts import render

from .models import User
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            user = User.objects.create_user