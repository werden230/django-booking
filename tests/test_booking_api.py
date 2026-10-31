import pytest
from rest_framework.test import APIClient

from booking_service.models import Booking, Room

BOOKING_URL = "/api/v1/booking/"


@pytest.mark.django_db
class TestBookingAPI:
    def test_get_bookings(self, api_client: APIClient, booking: Booking):
        response = api_client.get(BOOKING_URL)

        assert response.status_code == 200
        assert len(response.data) == 1

    def test_bookings_sorted_by_date(
        self,
        api_client: APIClient,
        room: Room,
        booking: Booking,
    ):
        earlier_booking = Booking.objects.create(
            room=room,
            date_from="2026-10-20",
            date_to="2026-10-25",
        )

        response = api_client.get(BOOKING_URL)

        assert response.status_code == 200
        assert response.data[0]["id"] == earlier_booking.pk
        assert response.data[1]["id"] == booking.pk

    def test_create_booking(self, api_client: APIClient, room: Room):
        payload = {
            "room": room.pk,
            "date_from": "2026-11-10",
            "date_to": "2026-11-15",
        }

        response = api_client.post(BOOKING_URL, payload, format="json")

        assert response.status_code == 201
        assert "booking_id" in response.data
        assert Booking.objects.filter(pk=response.data["booking_id"]).exists()

    def test_create_overlapping_booking(
        self,
        api_client: APIClient,
        booking: Booking,
        room: Room,
    ):
        payload = {
            "room": room.pk,
            "date_from": "2026-11-03",
            "date_to": "2026-11-07",
        }

        response = api_client.post(BOOKING_URL, payload, format="json")

        assert response.status_code == 400
        assert response.data["error"] == "Booking intersection occured!"

    def test_create_booking_for_another_room(
        self,
        api_client: APIClient,
        booking: Booking,
        another_room: Room,
    ):
        payload = {
            "room": another_room.pk,
            "date_from": "2026-11-03",
            "date_to": "2026-11-07",
        }

        response = api_client.post(BOOKING_URL, payload, format="json")

        assert response.status_code == 201

    def test_delete_booking(self, api_client: APIClient, booking: Booking):
        response = api_client.delete(f"{BOOKING_URL}{booking.pk}")

        assert response.status_code == 204
        assert not Booking.objects.filter(pk=booking.pk).exists()
