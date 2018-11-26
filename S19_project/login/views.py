from django.shortcuts import render,HttpResponse, redirect
from . import models

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        print(username, password)
        models.Userinfo.objects.create(username=username, password=password)
        return redirect('/account/login')
    elif request.method == 'GET':
        obj = models.Userinfo.objects.all()
        print(obj)
        return render(request, 'login/login.html', {'obj_info': obj})

def userdel(request, nid):
    print(request.method)
    models.Userinfo.objects.filter(pk=nid).delete()
    return redirect('/account/login')

def userinfo(request, nid):
    obj=models.Userinfo.objects.filter(pk=nid).first()
    print(obj)
    return render(request, 'login/userinfo.html', {'user_info': obj})

def userupdate(request, nid):
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        models.Userinfo.objects.filter(pk=nid).update(username=username, password=password)
        return redirect('/account/login')
    if request.method == "GET":
        obj = models.Userinfo.objects.filter(pk=nid).first()
        return render(request, "login/userupdate.html", {'obj': obj})
