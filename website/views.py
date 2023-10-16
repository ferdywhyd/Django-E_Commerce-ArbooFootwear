from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Product

# Create your views here.

def home(request):
    return render(request, "home.html", {})

def product(request):
    return render(request, "product.html", {})

def our_story(request):
    return render(request, "our_story.html", {})

def login_user(request):
    customer = Customer.objects.all()
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
        return render(request, "login.html", {'customer':customer})
    
def logout_user(request):
    logout(request)
    messages.success(request, "Berhasil Logout")
    return redirect('home')

def product(request):
    products = Product.objects.all()
    return render(request, "product.html", {'products':products})