from rest_framework import serializers

from .models import Booking, Room


class RoomSerializer(serializers.ModelSerializer[Room]):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer[Booking]):
    class Meta:
        model = Booking
        fields = "__all__"
