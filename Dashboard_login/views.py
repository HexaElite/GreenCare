from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def maindashboard(request):
    return render(request, 'maindashboard.html',{})


 
# Render login page
def login_page(request):
    return render(request, 'login.html', {})


def login_user(request):
    if request.method == "POST":
        # Get the username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print("Authenticated User:", user)  # Debugging

        if user is not None:
            # Log the user in
            login(request, user)
            
            # Role-specific greeting or general success message
            messages.success(request, f"Welcome!")
            return redirect('maindashboard')  # Redirect to the dashboard
        else:
            # Display error if authentication fails
            messages.error(request, "Invalid username or password")
            return redirect('login')  # Redirect to login page
    else:
        # Render the login page for GET requests
        return render(request, 'login.html', {})
 
def logout_user(request):
    logout(request)
    messages.success(request, ("you have been logged out..."))
    return redirect('login')