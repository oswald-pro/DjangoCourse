from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="home"),
    path('login', views.login, name="login"),
    path('signup', views.index, name="signup"),

]