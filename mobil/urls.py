from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_mobil, name='list'),
    path('tambah_mobil/', views.tambah_mobil, name='tambah_mobil'),
    path('mobil/<int:pk>/detail_mobil/', views.detail_mobil, name='detail_mobil'),
    path('mobil/<int:pk>/edit_mobil/', views.edit_mobil, name='edit_mobil'),
    path('mobil/<int:pk>/tambah_service/', views.tambah_service, name='tambah_service'),
    path('mobil/<int:pk>/hapus/', views.hapus_mobil, name='hapus_mobil'),
]