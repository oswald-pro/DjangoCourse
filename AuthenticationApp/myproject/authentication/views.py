from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'UserAuth/index.html')


def home(request):
    return render(request, 'UserAuth/home.html')


def my_login(request):
    if request.method == 'POST':
        LoginUsername = request.POST['username']
        LoginPassword = request.POST['password']

        user = authenticate(username=LoginUsername, password=LoginPassword)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "UserAuth/home.html", {'fname': fname})

        else:
            messages.error(request, "Invalid username or password")
            return redirect("index")

    return render(request, 'UserAuth/login.html')


def register(request):

    if request.method == 'POST':
        # Username = request.POST.get('Username')
        Username = request.POST['username']
        Firstname = request.POST['firstname']
        Lastname = request.POST['lastname']
        Email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        myuser = User.objects.create_user(Username, Email, Password1)
        myuser.first_name = Firstname
        myuser.last_name = Lastname

        myuser.save()

        messages.success(request, "User created successfully!!!")
        return redirect('login')

    return render(request, "UserAuth/register.html")


def logout(request):
    pass