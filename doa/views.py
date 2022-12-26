from django.shortcuts import render, redirect
from blog.models import Info, Doa
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from . import forms
from django.contrib import messages
import requests
from django.http import HttpResponse

def index(request):
    template_name = 'front/index.html'
    context = {
        'title':'halaman index'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title':'halaman about'
    }
    return render(request, template_name, context)

def doa(request):
    template_name = 'front/doa.html'
    # response=requests.get('https://doa-doa-api-ahmadramadhan.fly.dev/api').json()
    # for i in response:
    #     if Doa.objects.filter(doa=i['doa']).exists() == False:
    #         Doa.objects.create(doa=i['doa'],ayat=i['ayat'],latin=i['latin'],artinya=i['artinya'])
    #     else:
    #         Doa.objects.filter(doa=i['doa']).update(doa=i['doa'],ayat=i['ayat'],latin=i['latin'],artinya=i['artinya'])
    response = Doa.objects.all()
    context = {
        'title':'halaman doa',
        'response':response
    }
    return render(request, template_name, context)

def blog(request):
    template_name = 'front/blog.html'
    info = Info.objects.all()
    context = {
        'title':'halaman blog',
        'info' :info,
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'front/contact.html'
    context = {
        'title':'halaman contact'
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        print('Telah Berhasil Login')
        return redirect ('index')
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #data ditemukan
            print('username benar')
            auth_login(request, user)
            return redirect('index')
        else:
            #data tidak ditemukan
            print('username salah')
    
    context = {
        'title' : 'Form Login',
    }
    return render(request, template_name, context)

def register(request):
    template_name = 'account/register.html'
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if request.POST.get('password1') == request.POST.get('password2'):
            if form.is_valid():
                user_new = form.save()
                messages.success(request, "Anda Telah Berhasil Melakukan Register, Sekarang anda telah login")
                return redirect('index')
        else:
            return redirect('register')

    context = {
        'title' : 'Form Register',
        'form':form
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect ('index')