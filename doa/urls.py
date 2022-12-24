from django.contrib import admin
from django.urls import path, include
from doa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('blog.urls')),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('doa', doa, name='doa'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
