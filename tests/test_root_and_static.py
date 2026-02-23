import pytest


@pytest.mark.asyncio
async def test_root_redirect(client):
    # Arrange: client fixture
    # Act
    resp = await client.get("/", follow_redirects=False)

    # Assert
    assert resp.status_code in (301, 302, 307, 308)
    assert resp.headers.get("location") == "/static/index.html"


@pytest.mark.asyncio
async def test_static_index_served(client):
    # Act
    resp = await client.get("/static/index.html")

    # Assert
    assert resp.status_code == 200
    assert "Mergington High School" in resp.text
