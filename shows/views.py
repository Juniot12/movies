from django.shortcuts import render,HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import users,admin,bookingdetails,moviedetails


# Create your views here.
def index(request):
    return render(request,"index.html")

def admin(request):
    return render(request,"admin.html")

def adfun(request):
    return render(request,"adfun.html")

def ad(request):
   



def de(request):
    return render(request,"de.html")

def upd(request):
    return render(request,"upd.html")



def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def booking(request):
    return render(request,"booking.html")









