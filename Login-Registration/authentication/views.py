from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "userAuth/index.html")


def login(request):
    return render(request, "userAuth/login.html")


def signup(request):
    return render(request, "userAuths/signup.html")


def logout(request):
    pass