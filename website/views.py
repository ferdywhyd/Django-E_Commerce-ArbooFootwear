from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Product, Karyawan
from .forms import AddKaryawanForm
from django.core.paginator import Paginator

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
    sort = request.GET.get('sort', 'id') #untuk sortir table secara default
    karyawans = Karyawan.objects.all().order_by(sort)
    form = AddKaryawanForm(request.POST or None)
    page_number = request.GET.get('page',1)
    paginator = Paginator(karyawans, 10) #atur jumlah page di table
    page_karyawan = paginator.get_page(page_number)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Berhasil ditambahkan")
                return redirect('karyawan')
        context = {'form':form,
                   'karyawans':karyawans,
                   'page_karyawan':page_karyawan,
                   'sort':sort
                   }
        return render(request, "admin/karyawan.html", context)
    else:
        messages.success(request, "Kamu harus login brader")
        return redirect('home')
    
def delete_karyawan(request, pk):
    if request.user.is_authenticated:
        delete_user = Karyawan.objects.get(id=pk)
        delete_user.delete()
        messages.success(request, "Berhasil Dihapuss dari kenyataan")
        return redirect('karyawan')
    else:
        messages.success(request, "Kamu harus Login Braderrr")
        return redirect('home')
    
    
def gajian_karyawan(request):
    return render(request, 'admin/gajian_karyawan.html',{})


def dashboard(request):
    return render(request, "admin/dashboard.html", {})