from django.urls import path

from . import views

urlpatterns = [
    path('info/', views.info),
    path('host/', views.host),
    path('test_ajax/', views.test_ajax),
]
