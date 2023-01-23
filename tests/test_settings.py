"""Test settings from app"""
from core.settings import Settings


def test_development_config(app):
    """Test env development"""
    settings = Settings()
    assert app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == settings.SQLALCHEMY_DATABASE_URI


def test_testing_config(app):
    """Test env development"""
    settings = Settings()
    app.testing = True
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == settings.SQLALCHEMY_DATABASE_URI