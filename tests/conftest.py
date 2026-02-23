import copy
import pytest
from httpx import AsyncClient
try:
    # httpx >= 0.23 provides ASGITransport
    from httpx import ASGITransport
except Exception:
    ASGITransport = None

from src.app import app, activities


@pytest.fixture(scope="session")
async def client():
    if ASGITransport is None:
        # Fallback: create a normal client (will attempt network requests)
        async with AsyncClient(base_url="http://test") as ac:
            yield ac
    else:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac


@pytest.fixture(autouse=True)
def reset_activities():
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original))
