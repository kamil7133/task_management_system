import pytest
from app import create_app, db
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:" # memory base

@pytest.fixture
def test_client():
    app = create_app()
    app.config.from_object(TestConfig)

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
