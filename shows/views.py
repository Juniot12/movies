from django.shortcuts import render,HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import users,admin,bookingdetails,moviedetails


# Create your views here.
def index(request):
    return render(request,"index.html")

def adminPage(request):
    if request.method == "POST":
        try:
            name=request.POST["username"]
            ad = admin.objects.get(aname=name)
            if ad.pwd == request.POST["password"]:
                return HttpResponseRedirect("./adminfunctions.html")
            else:
                return HttpResponse("Incorrect Password")
        except Exception:
            return HttpResponse("Incorrect Password or Incorrect Username")
        
    return render(request,"admin.html")

def adfun(request):
    return render(request,"adfun.html")

def ad(request):
    if request.method == "POST":
        Moname=request.POST["moviename"]
        date_release=request.POST["releDate"]
        rating=request.POST["rating"]
        theatre_name=request.POST["theatreName"]
        seat_available=request.POST["seatAvail"]
        seatAvail=request.POST["seatAvail"]
        language=request.POST["lang"]
        md=moviedetails(Moname=Moname,date_release=date_release,rating=rating,theatre_name=theatre_name,seat_available=seat_available,language=language,seatAvail=seatAvail)
        md.save()
        return HttpResponseRedirect("./adminfunctions.html")
    return render(request,"ad.html")



def de(request):
    if request.method == "POST":
        Moname=request.POST["deleteMovie"]
        mh = moviedetails.objects.get(Moname=Moname)
        mh.delete()
        return HttpResponseRedirect("./adminfunctions.html")
    return render(request,"de.html")

def upd(request):
    if request.method == "POST":
        Moname=request.POST["movieName"]
        seat_available=request.POST["availableSeats"]
        mh = moviedetails.objects.get(Moname=Moname)
        mh.seat_available=seat_available
        mh.seatAvail=seat_available
        mh.save()
        return HttpResponseRedirect("./adminfunctions.html")
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
    if request.method == "POST":
        Name=request.POST["username"]
        age=request.POST["age"]
        gender=request.POST["question"]
        phonennumber=request.POST["mobile_no"]
        email=request.POST ["email"]
        password=request.POST["password"]
        us = users(Name=Name,age=age,gender=gender,phonennumber=phonennumber,email=email,password=password)
        us.save()
        return HttpResponseRedirect("user_login_new.html")
    return render(request,"signup.html")

def booking(request):
    if request.method == "POST":
        print(type(request.POST["seatClass"]))
        Mname=request.POST["movie"]
        theatre_name=request.POST["theatre"]
        no_oftickets=request.POST["seatClass"]
        day=request.POST["date"]
        time=request.POST["time"]
        try:
            md = moviedetails.objects.get(Moname=Mname,theatre_name=theatre_name,date_release=day)
            if int(no_oftickets) > 0 and request.POST["date"]!="" and int(no_oftickets)<=md.seatAvail:
                bd = bookingdetails(Mname=Mname,theatre_name=theatre_name,no_oftickets=no_oftickets,day=day,time=time)
                bd.save()
                md.seatAvail-= int(no_oftickets)
                md.save() 
                return HttpResponse("Your Tickets have been confirmed")
            elif int(no_oftickets)>md.seatAvail:
                return HttpResponse("No Available Seats")
        except Exception as e:
            return HttpResponse("No Movie Availble at theatre or at that time")

        
    md = moviedetails.objects.all()
    return render(request,"booking.html",{"md":md})










