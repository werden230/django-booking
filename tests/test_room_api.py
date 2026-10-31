import pytest
from rest_framework.test import APIClient

from booking_service.models import Room

ROOM_URL = "/api/v1/room/"


@pytest.mark.django_db
class TestRoomAPI:
    def test_get_rooms(self, api_client: APIClient, room: Room):
        response = api_client.get(ROOM_URL)

        assert response.status_code == 200
        assert len(response.data) == 1

    def test_sort_rooms_by_price_ascending(
        self,
        api_client: APIClient,
        room: Room,
        another_room: Room,
    ):
        response = api_client.get(ROOM_URL, {"sort_by": "price", "order": "asc"})

        assert response.status_code == 200
        assert response.data[0]["price"] == 100
        assert response.data[1]["price"] == 200

    def test_sort_rooms_by_price_descending(
        self,
        api_client: APIClient,
        room: Room,
        another_room: Room,
    ):
        response = api_client.get(ROOM_URL, {"sort_by": "price", "order": "desc"})

        assert response.status_code == 200
        assert response.data[0]["price"] == 200
        assert response.data[1]["price"] == 100

    def test_invalid_sort_field(
        self,
        api_client: APIClient,
        room: Room,
        another_room: Room,
    ):
        response = api_client.get(ROOM_URL, {"sort_by": "invalid_field"})

        assert response.status_code == 200
        assert len(response.data) == 2

    def test_invalid_sort_order(
        self,
        api_client: APIClient,
        room: Room,
        another_room: Room,
    ):
        response = api_client.get(ROOM_URL, {"sort_by": "price", "order": "invalid"})

        assert response.status_code == 200
        assert response.data[0]["price"] == 100

    def test_create_room(self, api_client: APIClient):
        payload = {
            "name": "New room",
            "description": "New description",
            "price": 150,
        }

        response = api_client.post(ROOM_URL, payload, format="json")

        assert response.status_code == 201
        assert "room_id" in response.data
        assert Room.objects.filter(pk=response.data["room_id"]).exists()

    def test_delete_room(self, api_client: APIClient, room: Room):
        response = api_client.delete(f"{ROOM_URL}{room.pk}")

        assert response.status_code == 204
        assert not Room.objects.filter(pk=room.pk).exists()
