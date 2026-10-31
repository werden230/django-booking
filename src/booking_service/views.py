from typing import Any

from django.db.models import QuerySet
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer


class RoomAPIView(generics.DestroyAPIView[Room], generics.ListCreateAPIView[Room]):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self) -> QuerySet[Room, Room]:
        queryset = super().get_queryset()

        sort_by = self.request.query_params.get("sort_by")
        order = self.request.query_params.get("order", "asc")

        allowed_fields = ("price", "created_at")

        if sort_by not in allowed_fields:
            return queryset

        if order not in ("asc", "desc"):
            order = "asc"

        if order == "desc":
            sort_by = f"-{sort_by}"

        return queryset.order_by(sort_by)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().create(request, *args, **kwargs)

        return Response(
            {"room_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )


class BookingAPIView(generics.DestroyAPIView[Booking], generics.ListCreateAPIView[Booking]):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self) -> QuerySet[Booking, Booking]:
        return Booking.objects.order_by("date_from")

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:

        data = request.data

        if not isinstance(data, dict):
            return Response(
                {"error": "Expected a JSON object."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        date_from = data.get("date_from")
        date_to = data.get("date_to")
        room = data.get("room")

        intersection = Booking.objects.filter(
            date_from__lte=date_to, date_to__gte=date_from, room=room
        )

        if intersection.exists():
            return Response(
                {"error": "Booking intersection occured!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response = super().create(request, *args, **kwargs)

        return Response(
            {"booking_id": response.data["id"]},
            status=status.HTTP_201_CREATED,
        )
