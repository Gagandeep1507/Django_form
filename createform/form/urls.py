from django.contrib import admin
from django.urls import path
from form import views

urlpatterns = [
    path('contact/',views.Contact,name="Contact"),
   
]
