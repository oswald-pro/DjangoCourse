from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'UserAuth/index.html')


def home(request):
    return render(request, 'UserAuth/home.html')


def signup(request):
    return render(request, 'UserAuth/signup.html')


def login(request):
    return render(request, 'UserAuth/login.html')


def logout(request):
    pass