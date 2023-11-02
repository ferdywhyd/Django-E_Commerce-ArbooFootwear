from django.db import models
import datetime

# Create your models here.
# category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#produk
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True)
    image = models.ImageField(upload_to='uploads/product')

    def __str__(self):
        return self.name

#order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=250, default='', blank=True)
    phone = models.CharField(max_length=12, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
    

# ADMIN DASBOARD

PEKERJAAN = ( 
    ('MARKETING','marketing'),
    ('ADMIN','admin'),
    ('DESAINER POLA','desainer pola'),
    ('JAHIT','jahit'),
    ('TARIK SOL','tarik sol')
)
class Karyawan(models.Model):
    nama = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=20, choices=PEKERJAAN)
    alamat = models.CharField(max_length=250, default='', blank=True)
    no_hp = models.CharField(max_length=13, default='', blank=True)

    def __str__(self):
        return self.nama
    
#Gajian Karyawan

class GajianKaryawan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nama = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    pekerjaan = models.CharField(max_length=20, choices=PEKERJAAN)
    produk = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(null=False, blank=False)
