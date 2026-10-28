from django.contrib import admin

from .models import Booking, Room

admin.site.register([Booking, Room])
# Register your models here.
