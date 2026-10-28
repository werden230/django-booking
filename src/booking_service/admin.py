from django.contrib import admin

from .models import Booking, Hotel, Room

admin.site.register([Hotel, Booking, Room])
# Register your models here.
