from src.main import app
from fastapi.testclient import TestClient
from datetime import datetime

FIXED_TOKEN = "token"
HEADERS = {"Authorization": FIXED_TOKEN}
NO_ADM_HEADERS = {"Authorization": "noadm_token"}
WRONG_HEADERS = {"Authorization": "wrong_token"}

client = TestClient(app)


def test_register_new_receipt_correctly_returns_201():
    response = client.post(
        "/receipts",
        headers=HEADERS,
        json={
            "products": {
                "tomatoes": 50,
                "bell pepper": 45
            },
            "supplier_id": "id",
            "timestamp": datetime.utcnow()
        }
    )

    assert response.status_code == 201


def test_register_new_receipt_with_wrong_info_returns_400():
    response = client.post(
        "/receipts",
        headers=HEADERS,
        json={
            "products": {
                "tomatoes": 50,
                "bell pepper": 45
            },
            "supplier_id": 5,
            "timestamp": datetime.utcnow()
        }
    )

    assert response.status_code == 400


def test_register_new_receipt_with_missing_data_returns_400():
    response = client.post(
        "/receipts",
        headers=HEADERS,
        json={
            "products": {
                "tomatoes": 50,
                "bell pepper": 45
            },
            "supplier_id": "id"
        }
    )

    assert response.status_code == 400


def test_register_new_receipt_with_invalid_token_returns_401():
    response = client.post(
        "/receipts",
        headers=WRONG_HEADERS,
        json={
            "products": {
                "tomatoes": 50,
                "bell pepper": 45
            },
            "supplier_id": "id",
            "timestamp": datetime.utcnow()
        }
    )

    assert response.status_code == 401


def test_register_new_receipt_with_no_token_returns_401():
    response = client.post(
        "/receipts",
        json={
            "products": {
                "tomatoes": 50,
                "bell pepper": 45
            },
            "supplier_id": "id",
            "timestamp": datetime.utcnow()
        }
    )

    assert response.status_code == 401


def test_list_receipts_last_24_hours_correctly_returns_200():
    response = client.get(
        "/receipts/last-24-hours",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_24_hours_filtering_by_supplier_correctly_returns_200():
    response = client.get(
        "/receipts/last-24-hours/new-day-flour",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_24_hours_filtering_by_non_existing_supplier_returns_404():
    response = client.get(
        "/receipts/last-24-hours/testsupplier",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_list_receipts_last_24_hours_with_invalid_token_returns_401():
    response = client.get(
        "/receipts/last-24-hours/new-day-flour",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_list_receipts_last_24_hours_with_no_token_returns_401():
    response = client.get(
        "/receipts/last-24-hours/new-day-flour"
    )

    assert response.status_code == 401


def test_list_receipts_last_week_returns_200():
    response = client.get(
        "/receipts/last-week",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_week_filtering_by_supplier_correctly_returns_200():
    response = client.get(
        "/receipts/last-week/new-day-flour",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_week_filtering_by_non_existing_supplier_returns_404():
    response = client.get(
        "/receipts/last-week/testsupplier",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_list_receipts_last_week_with_invalid_token_returns_401():
    response = client.get(
        "/receipts/last-week/new-day-flour",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_list_receipts_last_week_with_no_token_returns_401():
    response = client.get(
        "/receipts/last-week/new-day-flour"
    )

    assert response.status_code == 401


def test_list_receipts_last_month_returns_200():
    response = client.get(
        "/receipts/last-month",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_month_filtering_by_supplier_correctly_returns_200():
    response = client.get(
        "/receipts/last-month/new-day-flour",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_month_filtering_by_non_existing_supplier_returns_404():
    response = client.get(
        "/receipts/last-month/testsupplier",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_list_receipts_last_month_with_invalid_token_returns_401():
    response = client.get(
        "/receipts/last-month/new-day-flour",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_list_receipts_last_month_with_no_token_returns_401():
    response = client.get(
        "/receipts/last-month/new-day-flour"
    )

    assert response.status_code == 401


def test_list_receipts_last_year_returns_200():
    response = client.get(
        "/receipts/last-year",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_year_filtering_by_supplier_correctly_returns_200():
    response = client.get(
        "/receipts/last-year/new-day-flour",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_last_year_filtering_by_non_existing_supplier_returns_404():
    response = client.get(
        "/receipts/last-year/testsupplier",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_list_receipts_last_year_with_invalid_token_returns_401():
    response = client.get(
        "/receipts/last-year/new-day-flour",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_list_receipts_last_year_with_no_token_returns_401():
    response = client.get(
        "/receipts/last-year/new-day-flour"
    )

    assert response.status_code == 401


def test_list_receipts_older_than_a_year_returns_200():
    response = client.get(
        "/receipts/older-than-a-year",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_older_than_a_year_filtering_by_supplier_correctly_returns_200():
    response = client.get(
        "/receipts/older-than-a-year/new-day-flour",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_list_receipts_older_than_a_year_filtering_by_non_existing_supplier_returns_404():
    response = client.get(
        "/receipts/older-than-a-year/testsupplier",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_list_receipts_older_than_a_year_with_invalid_token_returns_401():
    response = client.get(
        "/receipts/older-than-a-year/new-day-flour",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_list_receipts_older_than_a_year_with_no_token_returns_401():
    response = client.get(
        "/receipts/older-than-a-year/new-day-flour"
    )

    assert response.status_code == 401


def test_get_receipt_by_existing_id_returns_200():
    response = client.get(
        "/receipts/idteste",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_get_receipt_by_non_existing_id_returns_404():
    response = client.get(
        "/receipts/idteste",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_get_receipt_by_id_with_invalid_token_returns_401():
    response = client.get(
        "/receipts/idteste",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_get_receipt_by_id_with_no_token_returns_401():
    response = client.get(
        "/receipts/idteste"
    )

    assert response.status_code == 401


def test_update_receipt_correctly_returns_200():
    response = client.put(
        "/receipts/idteste",
        headers=HEADERS,
        json={
            "products": {
                "bell pepper": 40
            }
        }
    )

    assert response.status_code == 200


def test_update_receipt_that_does_not_exist_returns_404():
    response = client.put(
        "/receipts/idteste",
        headers=HEADERS,
        json={
            "products": {
                "bell pepper": 40
            }
        }
    )

    assert response.status_code == 404


def test_update_receipt_correctly_with_no_admin_privilege_returns_403():
    response = client.put(
        "/receipts/idteste",
        headers=NO_ADM_HEADERS,
        json={
            "products": {
                "bell pepper": 40
            }
        }
    )

    assert response.status_code == 403


def test_update_receipt_incorrectly_returns_400():
    response = client.put(
        "/receipts/idteste",
        headers=HEADERS,
        json={
            "products": {
                "bell pepper": []
            }
        }
    )

    assert response.status_code == 400


def test_update_receipt_incorrectly_with_no_admin_privilege_returns_403():
    response = client.put(
        "/receipts/idteste",
        headers=NO_ADM_HEADERS,
        json={
            "products": {
                "bell pepper": []
            }
        }
    )

    assert response.status_code == 403


def test_update_receipt_with_invalid_token_returns_401():
    response = client.put(
        "/receipts/idteste",
        headers=WRONG_HEADERS,
        json={
            "products": {
                "bell pepper": 40
            }
        }
    )

    assert response.status_code == 401


def test_update_receipt_with_no_token_returns_401():
    response = client.put(
        "/receipts/idteste",
        json={
            "products": {
                "bell pepper": 40
            }
        }
    )

    assert response.status_code == 401


def test_delete_receipt_by_existing_id_returns_204():
    response = client.delete(
        "/receipts/idteste",
        headers=HEADERS
    )

    assert response.status_code == 204


def test_delete_receipt_by_existing_id_with_no_admin_privilege_returns_403():
    response = client.delete(
        "/receipts/idteste",
        headers=NO_ADM_HEADERS
    )

    assert response.status_code == 403


def test_delete_receipt_by_non_existing_id_returns_404():
    response = client.delete(
        "/receipts/idteste",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_delete_receipt_by_non_existing_id_with_no_admin_privilege_returns_403():
    response = client.delete(
        "/receipts/idteste",
        headers=NO_ADM_HEADERS
    )

    assert response.status_code == 403


def test_delete_receipt_without_passing_id_returns_400():
    response = client.delete(
        "/receipts",
        headers=HEADERS
    )

    assert response.status_code == 400


def test_delete_receipt_with_invalid_token_returns_401():
    response = client.delete(
        "/receipts/idteste",
        headers=WRONG_HEADERS
    )

    assert response.status_code == 401


def test_delete_receipt_with_no_token_returns_401():
    response = client.delete(
        "/receipts/idteste"
    )

    assert response.status_code == 401
