from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from .forms import LoginForm, RegisterForm


# Create your views here.
def welcome_user(request):
    """Render index.html"""
    return render(request, 'index.html')


def register_user(request):
    """Register user and redirect to login page"""
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('registerapp:login_page'))
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'register_form': form})


def login_user(request):
    """Display login page and authenticate user"""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main_page'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'login_form': form})


def logout_user(request):
    """Log out user"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('index_page'))
