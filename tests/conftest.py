from fastapi.testclient import TestClient
from httpx import AsyncClient # used to make the requests 
import pytest 
from main import LogRecord 
from main import app 

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture()
def client():
    yield TestClient(app)

@pytest.fixture(autouse=True)
async def cleanup():
    LogRecord.clear()
    yield

#Where you need to use httpx to make requests
async def async_client(client):
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac