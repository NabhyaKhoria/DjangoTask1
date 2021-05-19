from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password = request.POST['pas']
        email = request.POST['emid']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            user.save()
            print("User created")
            return redirect('login')

    else:
        return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pas']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('hello')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def hello(request):
    return render(request,'hello.html')
