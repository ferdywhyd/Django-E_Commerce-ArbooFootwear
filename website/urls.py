from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/", views.product, name="product"),
    path("our_story/", views.our_story, name="our_story"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("karyawan/", views.karyawan, name="karyawan"),
    # path("add_karyawan/", views.add_karyawan, name="add_karyawan"),
    path("dashboard/", views.dashboard, name="dashboard"),
]