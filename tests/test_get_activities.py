import pytest


@pytest.mark.asyncio
async def test_get_activities_returns_dict(client):
    # Act
    resp = await client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


@pytest.mark.asyncio
async def test_activities_schema(client):
    # Act
    resp = await client.get("/activities")
    data = resp.json()

    # Assert
    for activity in data.values():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
