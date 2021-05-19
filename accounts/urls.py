from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('hello',views.hello, name='hello'),
    path('logout',views.logout, name='logout'),
]
