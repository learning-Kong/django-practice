from django.shortcuts import render_to_response, render,redirect
from .forms import UserForm, RegisterFrom
from . import models
import hashlib

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode('utf-8'))
    return h.hexdigest()    # update方法只接收bytes类型
def base(request):
    pass
    return render_to_response('login/base.html')

def index(request):
    pass
    return render_to_response('login/index.html')

def login(request):
    if request.session.get('is_login', None):
        print(request.session.items())
        return redirect('/account/index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "必须填写"
        if login_form.is_valid():   # 确保用户名和密码都不为空
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username, password)
            try:
                user = models.User.objects.get(name=username)
                print(user)
                if user.password == hash_code(password):    # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/account/index/')
                else:
                    message = '密码不正确'
            except Exception as e:
                print(e)
                message = '用户名不存在'
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.method == "POST":
        register_form = RegisterFrom(request.POST)
        message = "请输入填写内容"
        print(register_form)
        if register_form.is_valid():    #有数据，并进行处理
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:      #判断两次密码是否相同
                message = "两次密码不同，请重新输入密码"
                print(message)
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = "该用户已存在"
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱已存在"
                    return  render(request, "/login/register.html", locals())

                # 创建新用户
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)    # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/account/login/')
    register_form = RegisterFrom()
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/account/index/")
    request.session.flush()
    return render_to_response("login/index.html")