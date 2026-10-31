import pytest
from rest_framework.test import APIClient

from booking_service.models import Booking, Room


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def room() -> Room:
    return Room.objects.create(
        name="Test room",
        description="Test description",
        price=100,
    )


@pytest.fixture
def another_room() -> Room:
    return Room.objects.create(
        name="Another room",
        description="Another description",
        price=200,
    )


@pytest.fixture
def booking(room: Room) -> Booking:
    return Booking.objects.create(
        room=room,
        date_from="2026-11-01",
        date_to="2026-11-05",
    )
