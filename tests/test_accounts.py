import requests
from config import BASE_URL, TIMEOUT

VALID_CURRENCIES = {"USD", "EUR", "GBP", "ARS", "MXN", "BRL"}
VALID_ACCOUNT_TYPES = {"checking", "savings", "credit", "investment"}
VALID_STATUSES = {"active", "inactive", "frozen", "closed"}


def test_get_accounts_status_200(get_accounts):
    assert get_accounts.status_code == 200


def test_accounts_response_is_list(get_accounts):
    data = get_accounts.json()
    assert isinstance(data, list)


def test_accounts_not_empty(get_accounts):
    data = get_accounts.json()
    assert len(data) > 0


def test_account_has_required_fields(get_accounts):
    data = get_accounts.json()
    for account in data:
        assert "id" in account
        assert "accountNumber" in account
        assert "balance" in account
        assert "currency" in account


def test_account_balance_is_non_negative(get_accounts):
    data = get_accounts.json()
    for account in data:
        assert float(account["balance"]) >= 0, (
            f"Account {account['id']} has negative balance: {account['balance']}"
        )


def test_account_ids_are_unique(get_accounts):
    data = get_accounts.json()
    ids = [account["id"] for account in data]
    assert len(ids) == len(set(ids)), "Duplicate account IDs detected"


def test_account_currency_is_valid(get_accounts):
    data = get_accounts.json()
    for account in data:
        assert account["currency"] in VALID_CURRENCIES, (
            f"Invalid currency '{account['currency']}' in account {account['id']}"
        )


def test_account_number_is_non_empty_string(get_accounts):
    data = get_accounts.json()
    for account in data:
        assert isinstance(account["accountNumber"], str)
        assert len(account["accountNumber"]) > 0


def test_get_account_by_id():
    response = requests.get(f"{BASE_URL}/accounts/1", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_get_account_invalid_id_returns_404():
    response = requests.get(f"{BASE_URL}/accounts/99999", timeout=TIMEOUT)
    assert response.status_code == 404


def test_account_type_is_valid(get_accounts):
    data = get_accounts.json()
    for account in data:
        if "type" in account:
            assert account["type"] in VALID_ACCOUNT_TYPES, (
                f"Invalid account type '{account['type']}' in account {account['id']}"
            )


def test_account_status_is_valid(get_accounts):
    data = get_accounts.json()
    for account in data:
        if "status" in account:
            assert account["status"] in VALID_STATUSES, (
                f"Invalid status '{account['status']}' in account {account['id']}"
            )
