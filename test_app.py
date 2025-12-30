import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.data == b"Hello, World!"

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.data == b"OK"
