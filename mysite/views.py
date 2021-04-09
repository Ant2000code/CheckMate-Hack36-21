from django.shortcuts import render,redirect
#from . models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User,auth

from django.conf import settings
from django.core.mail import send_mail
import json


def about(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def home(request):
    return render(request, 'home.html')