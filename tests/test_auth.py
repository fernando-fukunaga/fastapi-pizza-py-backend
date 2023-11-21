from src.main import app
from fastapi.testclient import TestClient
from tests.random_number_generator import random_number

FIXED_TOKEN = "token"
HEADERS = {"Authorization": FIXED_TOKEN}
WRONG_HEADERS = {"Authorization": "wrong_token"}

client = TestClient(app)


def test_sign_up_correctly_returns_201():
    response = client.post(
        "/auth/sign-up",
        json={
            "email": f"testdummy{random_number()}@email.com",
            "password": "password"
        }
    )

    assert response.status_code == 201


def test_sign_up_with_existing_email_returns_400():
    response = client.post(
        "/auth/sign-up",
        json={
            "email": "fernando@email.com",
            "password": "password"
        }
    )

    assert response.status_code == 400


def test_sign_up_with_password_longer_than_14_chars_returns_400():
    response = client.post(
        "/auth/sign-up",
        json={
            "email": "fernando@email.com",
            "password": "password0000000"
        }
    )

    assert response.status_code == 400


def test_login_correctly_returns_200():
    response = client.post(
        "/auth/login",
        json={
            "email": "fernando@email.com",
            "password": "password"
        }
    )

    assert response.status_code == 400


def test_login_correctly_returns_a_token():
    response = client.post(
        "/auth/login",
        json={
            "email": "fernando@email.com",
            "password": "password"
        }
    )

    assert "access_token" in response.json


def test_login_with_wrong_email_returns_400():
    response = client.post(
        "/auth/login",
        json={
            "email": "fernando1@email.com",
            "password": "password"
        }
    )

    assert response.status_code == 400


def test_login_with_wrong_password_returns_400():
    response = client.post(
        "/auth/login",
        json={
            "email": "fernando@email.com",
            "password": "password1"
        }
    )

    assert response.status_code == 400


def test_me_route_with_valid_token_returns_200():
    response = client.get("/auth/me", headers=HEADERS)

    assert response.status_code == 200


def test_me_route_with_invalid_token_returns_401():
    response = client.get("/auth/me", headers=WRONG_HEADERS)

    assert response.status_code == 401


def test_me_route_with_no_token_token_returns_401():
    response = client.get("/auth/me")

    assert response.status_code == 401
