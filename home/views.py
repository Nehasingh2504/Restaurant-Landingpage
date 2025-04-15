from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from home.models import *
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def book_alert(request):
    messages.warning(request,'Login first before booking table!!...')
    return render(request,'home.html')

def book(request):
    return render(request,'book.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def home_after(request):
    return render(request,'home_after.html')

def insert_booking(request):
    name=request.GET['name']
    email=request.GET['email']
    date=request.GET['date']
    time=request.GET['time']
    rec=booktable(Name=name,Email=email,Date=date,Time=time)
    rec.save()
    return render(request,'book.html')

def signup_detail(request):
    email=request.GET['email']
    password=request.GET['password']
    if(signupdetails.objects.filter(Email=email).exists()):
        messages.warning(request,'email already exist')
    else:
        rec=signupdetails(Email=email,Password=password)
        rec.save()
    return render(request,'login.html')

def login_detail(request):
    email=request.GET['email']
    password=request.GET['password']
    if(signupdetails.objects.filter(Email=email).exists()== False):
        messages.warning(request,'Email doesnot exist plz signup first')
        return render(request,'login.html')
    elif(signupdetails.objects.filter(Email=email,Password=password).exists()):
        return render(request,'home_after.html')
    else:
        messages.warning(request,'wrong password or email or incase you doesnot sigup till now so plz signup first to continue..')
        return render(request,'login.html')