from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm


# Create your views here.


def index(request):
    """Return index.html page"""
    return render(request, 'index.html')


def logout(request):
    """Log user out"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(reverse('index'))


def login(request):
    """Return login page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in.")
            else:
                login_form.add_error(None,
                                     "Username or password is incorrect.")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
