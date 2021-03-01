import pytest

from delivery.app import create_app

@pytest.fixture(scope="module")
def app():
    """Instance os main flask app"""
    return create_app()

