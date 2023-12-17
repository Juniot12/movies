from django.contrib import admin as a

from .models import admin,moviedetails,users,bookingdetails

a.site.register(moviedetails)
a.site.register(users)
a.site.register(bookingdetails)
a.site.register(admin)

