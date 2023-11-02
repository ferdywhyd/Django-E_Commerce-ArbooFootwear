from django.contrib import admin
from .models import Customer, Category, Order, Product, Karyawan, GajianKaryawan

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)

# ADMIN DASBOARD
admin.site.register(Karyawan)
admin.site.register(GajianKaryawan)