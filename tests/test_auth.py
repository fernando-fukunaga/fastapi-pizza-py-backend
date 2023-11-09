from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_sign_up_correctly_returns_201():
    pass


def test_sign_up_with_existing_email_returns_400():
    pass


def test_sign_up_with_password_longer_than_14_chars_returns_400():
    pass


def test_login_correctly_returns_200():
    pass


def test_login_correctly_returns_a_token():
    pass


def test_login_with_wrong_username_returns_400():
    pass


def test_login_with_wrong_password_returns_400():
    pass


def test_me_route_with_valid_token_returns_200():
    pass


def test_me_route_with_invalid_token_returns_401():
    pass


def test_me_route_with_no_token_token_returns_401():
    pass
