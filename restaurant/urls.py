from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('qr-menu/', views.qr_menu, name='qr_menu'),
]
