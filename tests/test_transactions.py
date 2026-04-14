def test_get_transactions_status_200(get_transactions):
    assert get_transactions.status_code == 200


def test_transactions_response_is_list(get_transactions):
    data = get_transactions.json()
    assert isinstance(data, list)


def test_transaction_has_required_fields(get_transactions):
    data = get_transactions.json()

    for tx in data:
        assert "id" in tx
        assert "fromAccountId" in tx
        assert "toAccountId" in tx
        assert "amount" in tx
        assert "currency" in tx
        assert "status" in tx


def test_transaction_accounts_exist(get_transactions, get_accounts):
    transactions = get_transactions.json()
    accounts = get_accounts.json()

    account_ids = {int(acc["id"]) for acc in accounts}

    for tx in transactions:
        assert int(tx["fromAccountId"]) in account_ids
        assert int(tx["toAccountId"]) in account_ids