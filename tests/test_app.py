import pytest
from webapp.app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_sub(client):
    response = client.get("/sub?a=5&b=2")
    assert b"<p>The result is 3</p>" in response.data
    
def test_mult(client):
    response = client.get("/mult?a=5&b=3")
    assert b"<p>The result is 15</p>" in response.data
    
def test_add(client):
    response = client.get("/add?a=3&b=2")
    assert b"<p>The result is 5</p>" in response.data
    assert b"<p>The result is 32</p>" not in response.data

def test_home(client):
    response = client.get("/")
    assert b"<p>Hello World!</p>" in response.data