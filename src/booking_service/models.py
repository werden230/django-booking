from django.core.validators import MinValueValidator
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Room(models.Model):
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantiy = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])


class Booking(models.Model):
    room = models.ForeignKey("Room", on_delete=models.PROTECT)
    date_from = models.DateField()
    date_to = models.DateField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
