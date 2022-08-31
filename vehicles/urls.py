from django.contrib import admin
from django.urls import path

from . import views

app_name = 'vehicles'
urlpatterns = [
    path('', views.home, name="home"),
    path('vehicles/', views.vehicle, name="vehicle"),
    path('vehicles/<int:id>/', views.vehicle, name="sneaker"),
]
