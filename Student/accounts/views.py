from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime

# Create your views here.

user = User()


def login(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']

        global user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            return redirect('homepage')
        else:
            return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, "accounts/register.html")
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        print('User Saved')
        return redirect('/')


def homepage(request):
    print(user.date_joined)
    joinedDate=user.date_joined+datetime.timedelta(days=2)
    if  joinedDate.date() <= datetime.datetime.now().date():
        subscribe=False
    else:
        subscribe=True
    return render(request, 'accounts/homepage.html', {'userDet':user, 'subscribe':subscribe})


def logout(request):
    auth.logout
    return redirect('/')
