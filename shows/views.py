from django.shortcuts import render,HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import users,admin,bookingdetails,moviedetails


# Create your views here.
def index(request):
    return render(request,"index.html")

def adminPage(request):
    if request.method == "POST":
        name=request.POST["username"]
        ad = admin.objects.get(aname=name)
        if ad.pwd == request.POST["password"]:
            return HttpResponseRedirect("./adminfunctions.html")
        else:
            return HttpResponse("Incorrect Password")
        
    return render(request,"admin.html")

def adfun(request):
    return render(request,"adfun.html")

def ad(request):

    return render(request,"ad.html")



def de(request):
    return render(request,"de.html")

def upd(request):
    return render(request,"upd.html")



def login(request):
    
    if request.method == "POST":
        name=request.POST["username"]
        ad = users.objects.get(Name=name)
        if ad.password == request.POST["password"]:
            return HttpResponseRedirect("./booking.html")
        else:
            return HttpResponse("Incorrect Password")
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def booking(request):
    return render(request,"booking.html")










