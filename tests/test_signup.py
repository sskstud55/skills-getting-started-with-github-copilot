import pytest
from urllib.parse import quote

from src.app import activities


@pytest.mark.asyncio
async def test_signup_happy_path_adds_participant(client):
    # Arrange
    activity = "Tennis Club"
    email = "tester@example.com"

    # Act
    resp = await client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email in activities[activity]["participants"]


@pytest.mark.asyncio
async def test_signup_nonexistent_activity_404(client):
    # Act
    resp = await client.post("/activities/NoSuchActivity/signup", params={"email": "a@b.c"})

    # Assert
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_signup_already_signed_400(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    resp = await client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 400
