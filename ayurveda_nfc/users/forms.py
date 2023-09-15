from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from .models import *

class UserRegister(UserCreationForm):

    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
