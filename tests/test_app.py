import sys
import os
import pytest

# Add the parent directory to Python path so it can find 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Check that the homepage loads and contains expected content"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Random Cat" in response.data
    assert b"http.cat" in response.data
    assert b"Refresh for another cat" in response.data
