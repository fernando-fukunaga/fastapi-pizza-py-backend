from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_register_supplier_correctly_returns_201():
    pass


def test_register_supplier_with_wrong_values_returns_400():
    pass


def test_register_supplier_with_missing_data_returns_400():
    pass


def test_register_supplier_with_invalid_token_or_no_token_returns_401():
    pass


def test_list_suppliers_returns_200():
    pass


def test_list_suppliers_with_invalid_token_or_no_token_returns_401():
    pass


def test_get_supplier_by_name_that_exists_returns_200():
    pass


def test_get_supplier_by_name_that_does_not_exist_returns_404():
    pass


def test_get_supplier_without_passing_name_returns_400():
    pass


def test_get_supplier_by_name_with_invalid_token_or_no_token_returns_401():
    pass


def test_update_supplier_correctly_returns_200():
    pass


def test_update_supplier_correctly_with_no_admin_privilege_returns_401():
    pass


def test_update_supplier_uncorrectly_returns_400():
    pass


def test_update_supplier_unorrectly_with_no_admin_privilege_returns_401():
    pass


def test_update_supplier_with_invalid_token_or_no_token_returns_401():
    pass


def test_delete_supplier_by_name_that_exists_returns_204():
    pass


def test_delete_supplier_by_name_that_exists_with_no_admin_privilege_returns_204():
    pass


def test_delete_supplier_by_name_that_does_not_exist_returns_404():
    pass


def test_delete_supplier_by_name_that_does_not_exist_with_no_admin_privilege_returns_401():
    pass


def test_delete_supplier_without_passing_name_returns_400():
    pass


def test_delete_supplier_with_invalid_token_or_no_token_returns_401():
    pass

