from django.shortcuts import render

# Create your views here.

def maindashboard(request):
    return render(request, 'maindashboard.html',{})

def login(request):
    return render(request, 'login.html',{})
