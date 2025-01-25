import pytest
from zakupy_app import create_app, TestConfig
from datetime import datetime, timedelta

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
def test_dodaj_paragon(client):
    # Test poprawnego dodania paragonu
    data = {
        'data': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
        'sklep': 'Testowy Sklep',
        'cena': '99.99',
        'rabat': '10.0'
    }
    response = client.post('/paragony', json=data)
    assert response.status_code == 201
    assert 'id' in response.json

    # Test błędnych danych
    invalid_data = {'data': 'niepoprawna-data'}
    response = client.post('/paragony', json=invalid_data)
    assert response.status_code == 400

def test_lista_paragonow(client):
    # Dodanie testowych paragonów
    test_data = [
        {'data': '2025-01-01', 'sklep': 'Sklep A', 'cena': '50.0'},
        {'data': '2025-01-02', 'sklep': 'Sklep B', 'cena': '100.0'}
    ]
    for d in test_data:
        client.post('/paragony', json=d)

    # Pobranie listy paragonów
    response = client.get('/paragony')
    assert response.status_code == 200
    data = response.json
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['sklep'] == 'Sklep B'  # Sortowanie po dacie malejąco
    assert float(data[0]['laczna_cena']) == 100.0
    assert float(data[1]['laczna_cena']) == 50.0