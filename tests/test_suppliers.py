from src.main import app
from fastapi.testclient import TestClient

FIXED_TOKEN = "token"
HEADERS = {"Authorization": FIXED_TOKEN}
NO_ADM_HEADERS = {"Authorization": "noadm_token"}
WRONG_HEADERS = {"Authorization": "wrong_token"}

client = TestClient(app)


def test_register_supplier_correctly_returns_201():
    response = client.post(
        "suppliers/",
        headers=HEADERS,
        json={
            "name": "testsupplier",
            "phone": "0800-777-7000",
            "specialty": "any"
        }
    )

    assert response.status_code == 201


def test_register_supplier_with_wrong_values_returns_400():
    response = client.post(
        "suppliers/",
        headers=HEADERS,
        json={
            "name": 1,
            "phone": "0800-777-7000",
            "specialty": "any"
        }
    )

    assert response.status_code == 400


def test_register_supplier_with_missing_data_returns_400():
    response = client.post(
        "suppliers/",
        headers=HEADERS,
        json={
            "name": "testsupplier",
            "phone": "0800-777-7000"
        }
    )

    assert response.status_code == 400


def test_register_supplier_with_invalid_token_returns_401():
    response = client.post(
        "suppliers/",
        headers=WRONG_HEADERS,
        json={
            "name": "testsupplier",
            "phone": "0800-777-7000",
            "specialty": "any"
        }
    )

    assert response.status_code == 401


def test_register_supplier_with_no_token_returns_401():
    response = client.post(
        "suppliers/",
        json={
            "name": "testsupplier",
            "phone": "0800-777-7000",
            "specialty": "any"
        }
    )

    assert response.status_code == 401


def test_list_suppliers_returns_200():
    response = client.get("/suppliers", headers=HEADERS)

    assert response.status_code == 200


def test_list_suppliers_with_invalid_token_returns_401():
    response = client.get("/suppliers", headers=WRONG_HEADERS)

    assert response.status_code == 401


def test_list_suppliers_with_no_token_returns_401():
    response = client.get("/suppliers")

    assert response.status_code == 401


def test_get_supplier_by_name_that_exists_returns_200():
    response = client.get("/suppliers/new-day-flour", headers=HEADERS)

    assert response.status_code == 200


def test_get_supplier_by_name_that_does_not_exist_returns_404():
    response = client.get("/suppliers/python-rules", headers=HEADERS)

    assert response.status_code == 404


def test_get_supplier_by_name_with_invalid_token_returns_401():
    response = client.get("/suppliers/new-day-flour", headers=WRONG_HEADERS)

    assert response.status_code == 401


def test_get_supplier_by_name_with_no_token_returns_401():
    response = client.get("/suppliers/new-day-flour")

    assert response.status_code == 401


def test_update_supplier_correctly_returns_200():
    response = client.put(
        "suppliers/testsupplier",
        headers=HEADERS,
        json={
            "name": "testsupplier1",
            "phone": "0800-777-7500",
            "specialty": "any"
        }
    )

    assert response.status_code == 200


def test_update_supplier_correctly_with_no_admin_privilege_returns_403():
    response = client.put(
        "suppliers/testsupplier1",
        headers=NO_ADM_HEADERS,
        json={
            "name": "testsupplier2",
            "phone": "0800-777-7500",
            "specialty": "any"
        }
    )

    assert response.status_code == 403


def test_update_supplier_uncorrectly_returns_400():
    response = client.put(
        "suppliers/testsupplier1",
        headers=HEADERS,
        json={
            "name": 1,
            "phone": "0800-777-7500",
            "specialty": "any"
        }
    )

    assert response.status_code == 400


def test_update_supplier_with_invalid_token_returns_401():
    response = client.put(
        "suppliers/testsupplier1",
        headers=WRONG_HEADERS,
        json={
            "name": "testsupplier2",
            "phone": "0800-777-7500",
            "specialty": "any"
        }
    )

    assert response.status_code == 401


def test_update_supplier_with_no_token_returns_401():
    response = client.put(
        "suppliers/testsupplier1",
        json={
            "name": "testsupplier2",
            "phone": "0800-777-7500",
            "specialty": "any"
        }
    )

    assert response.status_code == 401


def test_delete_supplier_by_name_that_exists_returns_204():
    response = client.delete(
        "/suppliers/testsupplier1",
        headers=HEADERS
    )

    assert response.status_code == 204


def test_delete_supplier_by_name_that_exists_with_no_admin_privilege_returns_403():
    response = client.delete(
        "/suppliers/testsupplier1",
        headers=NO_ADM_HEADERS
    )

    assert response.status_code == 403


def test_delete_supplier_by_name_that_does_not_exist_returns_404():
    response = client.delete(
        "/suppliers/python-rules",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_delete_supplier_without_passing_name_returns_400():
    response = client.delete(
        "/suppliers",
        headers=HEADERS
    )

    assert response.status_code == 400


def test_delete_supplier_with_invalid_token_returns_401():
    response = client.delete(
        "/suppliers/testsupplier1",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_delete_supplier_with_no_token_returns_401():
    response = client.delete(
        "/suppliers/testsupplier1"
    )

    assert response.status_code == 401
