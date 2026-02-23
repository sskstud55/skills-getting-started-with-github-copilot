import pytest
from urllib.parse import quote

from src.app import activities


@pytest.mark.asyncio
async def test_remove_happy_path_removes_participant(client):
    # Arrange
    activity = "Basketball Team"
    email = "alex@mergington.edu"
    assert email in activities[activity]["participants"]

    # Act
    resp = await client.delete(f"/activities/{quote(activity)}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email not in activities[activity]["participants"]


@pytest.mark.asyncio
async def test_remove_nonexistent_activity_404(client):
    # Act
    resp = await client.delete("/activities/NoSuch/participants", params={"email": "a@b.c"})

    # Assert
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_remove_nonexistent_participant_404(client):
    # Act
    resp = await client.delete(f"/activities/{quote('Programming Class')}/participants", params={"email": "not-in-list@example.com"})

    # Assert
    assert resp.status_code == 404
