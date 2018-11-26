from django.urls import path,re_path
from .import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]