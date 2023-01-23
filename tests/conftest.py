"""Configuration test"""
import pytest


from app import create_app, db


@pytest.fixture(scope="session")
def app():
    """""Criando e configurando um nova instancia doo app para cada test."""
    app = create_app()
    with app.app_context():
        db.session.remove()
        db.drop_all()
        db.create_all()
    return app


@pytest.fixture(scope="session")
def client(app):
    """Um client test para o app."""
    return app.test_client()


@pytest.fixture(scope="session")
def finish_test(app):
    """"Finish tests"""
    with app.app_context():
        db.session.remove()
        db.drop_all()
