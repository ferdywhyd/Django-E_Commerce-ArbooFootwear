from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Product, Karyawan
from .forms import AddKaryawanForm

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
            return redirect('dashboard')
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

def karyawan(request):
    karyawans = Karyawan.objects.all()
    form = AddKaryawanForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Berhasil ditambahkan")
                return redirect('karyawan')
        context = {'form':form, 'karyawans':karyawans}
        return render(request, "admin/karyawan.html", context)
    else:
        messages.success(request, "Kamu harus login brader")
        return redirect('home')

# def add_karyawan(request):
#     karyawans = Karyawan.objects.all()
#     form = AddKaryawanForm(request.POST or None)
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Berhasil ditambahkan")
#                 return redirect('karyawan')
#         context = {'form':form, 'karyawans':karyawans}
#         return render(request, "admin/add_karyawan.html", context)
#     else:
#         messages.success(request, "Kamu harus login brader")
#         return redirect('home')


def dashboard(request):
    return render(request, "admin/dashboard.html", {})