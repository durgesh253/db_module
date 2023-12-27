# 4) What is Django URLs?make program to create django urls 

# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
]
