from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)

    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    return render(request, 'base.html')

def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'home.html', {'string': string})

def home2(request):
    List = ["HTML", "CSS", "jQuery", "python", "Django"]
    return render(request, 'home2.html', {'List':List})

def home3(request):
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request, 'home3.html', {'info_dict': info_dict})

def home4(request):
    List = map(str, range(100))
    return render(request, 'home4.html', {'List': List})
