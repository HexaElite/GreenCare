from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here

def registration(request):
    return render(request, 'registration.html',{})

def appointments(request):
    return render(request, 'appointments.html',{})