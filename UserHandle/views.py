from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User,auth

from django.conf import settings
from django.core.mail import send_mail
import json


#Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/chat')

        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')


# signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                detail = Detail.objects.create(
                    userName=username,

                )

                detail.save()
                subject = 'Registration done successfully'
                message = f'Hi {user.username}, thank you for registering with Ask me Anything.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/signup')
        return redirect('/home')
    else:
        return render(request, 'signup.html')

# logout
def logout(request):
    auth.logout(request)
    return redirect('/home')