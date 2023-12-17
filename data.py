import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviet.settings')
django.setup()
from shows.models import users,admin,bookingdetails,moviedetails

ob1=[users(Name="maria",age=20,gender="female",phonennumber=8845671234,email="mariafiju@gmail.com",password="maria3452"),users(Name="matthew paul",age=20,gender="male",phonennumber=88423253334,email="mathai12@gmail.com",password="matu1452")]
users.objects.bulk_create(ob1)


ob2=[admin(aname="Joe Joseph",pwd="joe1231"),admin(aname="Jaganath",pwd="soman1256")]
admin.objects.bulk_create(ob2)


ob3=[moviedetails(Moname="Animal",date_release="2023-12-01",rating=4.6,theatre_name="pvr kochi",seat_available=150,language="Hindi"),moviedetails(Moname="Kathal",date_release="2023-11-23",rating=3.0,theatre_name="vaneetha-vineetha",seat_available=200,language="Malayalam")]
moviedetails.objects.bulk_create(ob3)


