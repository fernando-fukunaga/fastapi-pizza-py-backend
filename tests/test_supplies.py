from src.main import app
from fastapi.testclient import TestClient

FIXED_TOKEN = "token"
HEADERS = {"Authorization": FIXED_TOKEN}
NO_ADM_HEADERS = {"Authorization": "noadm_token"}
WRONG_HEADERS = {"Authorization": "wrong_token"}

client = TestClient(app)


def test_patch_supply_amount_correctly_returns_200():
    response = client.patch(
        "/supplies/id",
        headers=HEADERS,
        json={
            "amount": 1
        }
    )

    assert response.status_code == 200


def test_patch_supply_amount_for_non_existing_supply_returns_404():
    response = client.patch(
        "/supplies/id",
        headers=HEADERS,
        json={
            "amount": 1
        }
    )

    assert response.status_code == 404


def test_patch_supply_amount_correctly_with_no_admin_privilege_returns_403():
    response = client.patch(
        "/supplies/id",
        headers=NO_ADM_HEADERS,
        json={
            "amount": 1
        }
    )

    assert response.status_code == 403


def test_patch_supply_amount_incorrectly_returns_400():
    response = client.patch(
        "/supplies/id",
        headers=HEADERS,
        json={
            "amount": []
        }
    )

    assert response.status_code == 400


def test_patch_supply_amount_incorrectly_with_no_admin_privilege_returns_403():
    response = client.patch(
        "/supplies/id",
        headers=NO_ADM_HEADERS,
        json={
            "amount": []
        }
    )

    assert response.status_code == 403


def test_patch_supply_amount_with_missing_data_returns_400():
    response = client.patch(
        "/supplies/id",
        headers=HEADERS,
        json={}
    )

    assert response.status_code == 400


def test_patch_supply_amount_with_invalid_token_returns_401():
    response = client.patch(
        "/supplies/id",
        headers=WRONG_HEADERS,
        json={
            "amount": 1
        }
    )

    assert response.status_code == 401


def test_patch_supply_amount_with_no_token_returns_401():
    response = client.patch(
        "/supplies/id",
        json={
            "amount": 1
        }
    )

    assert response.status_code == 401


def test_delete_supply_correctly_returns_200():
    response = client.delete(
        "/supplies/id",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_delete_supply_that_does_not_exist_returns_404():
    response = client.delete(
        "/supplies/id",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_delete_supply_correctly_with_no_admin_privilege_returns_403():
    response = client.delete(
        "/supplies/id",
        headers=NO_ADM_HEADERS
    )

    assert response.status_code == 403


def test_delete_supply_with_missing_data_returns_400():
    response = client.delete(
        "/supplies",
        headers=HEADERS
    )

    assert response.status_code == 400


def test_delete_supply_with_invalid_token_returns_401():
    response = client.delete(
        "/supplies/id",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_delete_supply_with_no_token_returns_401():
    response = client.delete(
        "/supplies/id"
    )

    assert response.status_code == 401
