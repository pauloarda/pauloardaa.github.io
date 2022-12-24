from django.shortcuts import render, redirect
from .models import Info, Kategori
from django.http import request
from django.contrib.auth.decorators import login_required, user_passes_test

from doa.forms import User
from django.contrib.auth.models import User

# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

    template_name = "back/base.html"
    context = {
        'title':'dashboard'
    }
    return render(request, template_name, context)

@login_required
def info(request):
    template_name = "back/tabel_info.html"
    info = Info.objects.all()
    # for a in info:
      #  print(a.nama,'-',a.judul,'-',a.kategory)
    context = {
        'title':'info',
        'info':info,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title':'users',
        'list_user':list_user
    }
    return render(request, template_name, context)

@login_required
def tambah_info(request):
    template_name = "back/tambah_info.html"
    kategory = Kategori.objects.all()
    print(kategory)
    if request.method == "POST":
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kategory = request.POST.get('kategory')

        #panggil kategori
        kat = Kategori.objects.get(nama=kategory)
        Info.objects.create(
            nama = nama,
            judul = judul,
            body = body,
            kategory=kat,
        )
        return redirect(info)
    context = {
        'title': 'tambah info',
        'kategory':kategory,
    }
    return render(request, template_name, context)

@login_required
def lihat_info(request, id):
    template_name = "back/lihat_info.html"
    info = Info.objects.get(id=id)
    context = {
        'title':'lihat info',
        'info': info,
    }
    return render(request, template_name, context)

@login_required
def edit_info(request, id):
    template_name = "back/edit_info.html"
    i = Info.objects.get(id=id)
    if request.method == "POST":
        judul = request.POST.get("judul")
        body = request.POST.get("body")
        #simpan data
        i.judul = judul
        i.body = body
        i.save()
        return redirect(info)

    context = {
        'title':'edit info',
        'info': i,
    }
    return render(request, template_name, context)

@login_required
def delete_info(request, id):
    Info.objects.get(id=id).delete()
    return redirect(info)