from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_hello_world(client):
    response = client.get('/')
    assert b'Hello CI/CD Pipeline' in response.data
