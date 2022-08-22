from django.contrib import admin
from django.urls import path,include
from .views import DoctorView

urlpatterns = [
    path('info/',DoctorView,name='doctorinfo'),
   
]
