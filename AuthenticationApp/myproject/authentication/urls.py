from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="home"),
    path('signup', views.index, name="signup"),
    path('login', views.login, name="login"),

]
