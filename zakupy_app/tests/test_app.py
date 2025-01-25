import pytest
from zakupy_app import create_app, TestConfig

@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        with app.app_context():
            from zakupy_app.extensions import db
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()
 
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "API Zakupy działa!".encode('utf-8') in response.data

def test_404_error(client):
    response = client.get('/non-existent-route')
    assert response.status_code == 404
    assert b"404 - Page Not Found" in response.data

def test_config_loading(client):
    assert client.application.config['TESTING'] == True
    assert 'SECRET_KEY' in client.application.config