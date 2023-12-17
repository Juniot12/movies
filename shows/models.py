from django.db import models

# Create your models here.
from django.db import models
class users(models.Model):
    Name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phonennumber=models.IntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=12)

class bookingdetails(models.Model):
         Mname=models.CharField(max_length=40)
         theatre_name=models.CharField(max_length=30)
         no_oftickets=models.IntegerField()
         day=models.DateField()
         time=models.TimeField()
         language=models.CharField(max_length=20)
         payment=models.IntegerField()

class admin(models.Model):
    aname=models.CharField(max_length=100)
    pwd=models.CharField(max_length=12)
    
class moviedetails(models.Model):
        Moname=models.CharField(max_length=100)
        date_release=models.DateField()
        rating=models.DecimalField(max_digits=3,decimal_places=2)
        theatre_name=models.CharField(max_length=50)
        seat_available=models.IntegerField()
        language=models.CharField(max_length=30)
        


    


    
