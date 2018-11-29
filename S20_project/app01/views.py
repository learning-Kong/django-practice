from django.shortcuts import render, HttpResponse, redirect
from . import models
import json
import re
import time

# Create your views here.

def info(request):
    if request.method == "POST":
        nid = request.POST.get('nid')
        v1 = models.Host.objects.get(nid=nid)
        ret = {'status': True, 'hostname': None, 'ip': None, 'port': None}
        print(11111)
        ret['hostname'] = v1.hostname
        ret['ip'] = v1.ip
        ret['port'] = v1.port
        return HttpResponse(json.dumps(ret))

def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        v2 = models.Business.objects.filter(id__gt=0)
        return render(request, "host.html", {'v1': v1, 'v2': v2})
    if request.method == "POST":
        name = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        b_id = request.POST.get('b_id')
        models.Host.objects.create(hostname=name, ip=ip, port=port, b_id=b_id)
        print(name, ip, port, b_id)
        print('submit')
        return redirect("/host/")
def test_ajax(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        return render(request, "host.html", {'v1': v1})
    if request.method == "POST":
        ret = {'status': True, 'error': None, 'data': None}
        try:
            name = request.POST.get('hostname')
            ip = request.POST.get('ip')
            port = request.POST.get('port')
            b_id = request.POST.get('b_id')
            chck_IP = re.match('^((25[0-5]|2[0-4]\d|[0-1]?\d?\d)\.){3}((25[0-5]|2[0-4]\d|[0-1]?\d?\d))$', ip)
            if chck_IP:
                models.Host.objects.create(hostname=name, ip=ip, port=port, b_id=b_id)
            else:
                print(name, ip, port, b_id)
                ret['status'] = False
                ret['error'] = 'ip格式错误'
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '请求错误'
        return HttpResponse(json.dumps(ret))
def edit_ajax(request):
    if request.method == "POST":
        try:
            ret = {'status': True, 'error': None, 'data': None}
            nid = request.POST.get('nid')
            name = request.POST.get('hostname')
            ip = request.POST.get('ip')
            port = request.POST.get('port')
            b_id = request.POST.get('b_id')
            chck_IP = re.match('^((25[0-5]|2[0-4]\d|[0-1]?\d?\d)\.){3}((25[0-5]|2[0-4]\d|[0-1]?\d?\d))$', ip)
            if chck_IP:
                models.Host.objects.filter(nid=nid).update(hostname=name, ip=ip, port=port, b_id=b_id)
            else:
                print(name, ip, port, b_id)
                ret['status'] = False
                ret['error'] = 'ip格式错误'
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '请求错误'
        return HttpResponse(json.dumps(ret))
def delete(request):
    if request.method == "POST":
        ret = {'status': True, 'error': None, 'data': None}
        nid = request.POST.get('nid')
        print(nid)
        models.Host.objects.filter(nid=nid).delete()
        return HttpResponse(json.dumps(ret))
