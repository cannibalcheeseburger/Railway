from django.contrib import admin
from .models import Trains,Booking,Users
# Register your models here.

admin.site.register(Trains)
admin.site.register(Booking)
admin.site.register(Users)