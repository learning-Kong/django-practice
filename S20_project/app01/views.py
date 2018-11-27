from django.shortcuts import render, HttpResponse, redirect
from . import models
# Create your views here.

def info(request):
    return HttpResponse('hello world')
def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        print(v1)
        return render(request, "host.html", {'v1': v1})
    if request.method == "POST":
        name = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        b_id = request.POST.get('b_id')
        # models.Host.objects.create(hostname=name, ip=ip, port=port, b_id=b_id)
        # print(name, ip, port, b_id)
        print('submit')
        return redirect("/host/")
def test_ajax(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        print(v1)
        return render(request, "host.html", {'v1': v1})
    if request.method == "POST":
        name = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        b_id = request.POST.get('b_id')
        # models.Host.objects.create(hostname=name, ip=ip, port=port, b_id=b_id)
        print(name, ip, port, b_id)
        return redirect("/host/")
