import pytest
from zakupy_app import create_app, db
from config import TestConfig

@pytest.fixture(scope='module')
def test_app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def test_client(test_app):
    return test_app.test_client()