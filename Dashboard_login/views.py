# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here
def maindashboard(request):
    return render(request, 'maindashboard.html',{})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('maindashboard')  # Redirect to a dashboard or home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})