from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get("username")
            return HttpResponseRedirect(reverse("login"))
    else:
        form = UserRegister()

    return render(request,"users/register.html",
    {
        "form":form,
    })

def login(request):
    return render(request,"users/login.html")