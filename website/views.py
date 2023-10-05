from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

# Create your views here.

def home(request):
    return render(request, "home.html", {})

def product(request):
    return render(request, "product.html", {})

def company(request):
    return render(request, "company.html", {})

def login_user(request):
    records = Record.objects.all()
    # check to see if logging
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Berhasil Login")
            return redirect('home')
        else:
            messages.success(request, "Username dan Password Salah")
            return redirect('login_user')
    else:
        return render(request, "login.html", {'records':records})
    
def logout_user(request):
    logout(request)
    messages.success(request, "Berhasil Logout")
    return redirect('home')