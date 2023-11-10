from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_register_new_receipt_correctly_returns_200():
    pass


def test_register_new_receipt_with_wrong_info_returns_400():
    pass


def test_register_new_receipt_with_missing_data_returns_400():
    pass


def test_register_new_receipt_with_invalid_token_returns_401():
    pass


def test_register_new_receipt_without_token_returns_401():
    pass


def test_list_receipts_last_24_hours_correctly_returns_200():
    pass


def test_list_receipts_last_24_hours_filtering_by_supplier_correctly_returns_200():
    pass


def test_list_receipts_last_24_hours_filtering_by_nonexisting_supplier_returns_404():
    pass


def test_list_receipts_last_24_hours_with_invalid_token_returns_401():
    pass


def test_list_receipts_last_24_hours_without_token_returns_401():
    pass


def test_list_receipts_last_week_returns_200():
    pass


def test_list_receipts_last_week_filtering_by_supplier_correctly_returns_200():
    pass


def test_list_receipts_last_week_filtering_by_nonexisting_supplier_returns_404():
    pass


def test_list_receipts_last_week_with_invalid_token_returns_401():
    pass


def test_list_receipts_last_week_without_token_returns_401():
    pass


def test_list_receipts_last_month_returns_200():
    pass


def test_list_receipts_last_month_filtering_by_supplier_correctly_returns_200():
    pass


def test_list_receipts_last_month_filtering_by_nonexisting_supplier_returns_404():
    pass


def test_list_receipts_last_month_with_invalid_token_returns_401():
    pass


def test_list_receipts_last_month_without_token_returns_401():
    pass


def test_list_receipts_last_year_returns_200():
    pass


def test_list_receipts_last_year_filtering_by_supplier_correctly_returns_200():
    pass


def test_list_receipts_last_year_filtering_by_nonexisting_supplier_returns_404():
    pass


def test_list_receipts_last_year_with_invalid_token_returns_401():
    pass


def test_list_receipts_last_year_without_token_returns_401():
    pass


def test_list_receipts_older_than_a_year_returns_200():
    pass


def test_list_receipts_older_than_a_year_filtering_by_supplier_correctly_returns_200():
    pass


def test_list_receipts_older_than_a_year_filtering_by_nonexisting_supplier_returns_404():
    pass


def test_list_receipts_older_than_a_year_with_invalid_token_returns_401():
    pass


def test_list_receipts_older_than_a_year_without_token_returns_401():
    pass


def test_get_receipt_by_existing_id_returns_200():
    pass


def test_get_receipt_by_nonexisting_id_returns_404():
    pass


def test_get_receipt_by_id_with_invalid_token_returns_401():
    pass


def test_get_receipt_by_id_without_token_returns_401():
    pass


def test_update_receipt_correctly_returns_200():
    pass


def test_update_receipt_correctly_with_no_admin_privilege_returns_403():
    pass


def test_update_receipt_uncorrectly_returns_400():
    pass


def test_update_receipt_unorrectly_with_no_admin_privilege_returns_403():
    pass


def test_update_receipt_with_invalid_token_returns_401():
    pass


def test_update_receipt_without_token_returns_401():
    pass


def test_delete_receipt_by_existing_id_returns_204():
    pass


def test_delete_receipt_by_existing_id_with_no_admin_privilege_returns_403():
    pass


def test_delete_receipt_by_nonexisting_id_returns_404():
    pass


def test_delete_receipt_by_nonexisting_id_with_no_admin_privilege_returns_403():
    pass


def test_delete_receipt_without_passing_id_returns_400():
    pass


def test_delete_receipt_with_invalid_token_returns_401():
    pass


def test_delete_receipt_without_token_returns_401():
    pass

