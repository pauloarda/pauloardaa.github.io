from django.urls import path, include
from blog.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('info/', info, name='tabel_info'),
    path('users', users, name='tabel_users'),
    path('info/tambah/', tambah_info, name='tambah_info'),
    path('info/lihat/<str:id>', lihat_info, name='lihat_info'),
    path('info/edit/<str:id>', edit_info, name='edit_info'),
    path('info/delete/<str:id>', delete_info, name='delete_info'),
]
