from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/", views.product, name="product"),
    path("our_story/", views.our_story, name="our_story"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),

    #karyawan
    path("karyawan/", views.karyawan, name="karyawan"),
    # path("update/<int:pk>", views.update_karyawan, name="update_karyawan"),
    path("delete/<int:pk>", views.delete_karyawan, name="delete_karyawan"),

    path("gajian_karyawan/", views.gajian_karyawan, name="gajian_karyawan"),
    path("dashboard/", views.dashboard, name="dashboard"),
]