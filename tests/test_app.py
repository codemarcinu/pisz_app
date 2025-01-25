def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "API Zakupy działa!".encode('utf-8') in response.data

def test_404_error(client):
    response = client.get('/non-existent-route')
    assert response.status_code == 404
    assert b"404 - Page Not Found" in response.data

def test_config_loading(app):
    assert app.config['TESTING'] == True
    assert 'SECRET_KEY' in app.config