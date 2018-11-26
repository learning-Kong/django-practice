from django.urls import path,re_path
from . import views

urlpatterns = [
    path('login/', views.login),
    re_path('userdel-(\d+)/', views.userdel),
    re_path('userinfo-(\d+)/', views.userinfo),
    re_path('userupdate-(\d+)', views.userupdate),
]
