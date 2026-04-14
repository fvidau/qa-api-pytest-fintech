def test_invalid_endpoint(get_invalid):
    assert get_invalid.status_code == 404


def test_transactions_not_empty(get_transactions):
    data = get_transactions.json()
    assert len(data) > 0


def test_transaction_types(get_transactions):
    data = get_transactions.json()

    for tx in data:
        assert isinstance(int(tx["id"]), int)
        assert isinstance(int(tx["amount"]), int)
        assert isinstance(tx["currency"], str)


def test_transaction_not_same_account(get_transactions):
    data = get_transactions.json()

    for tx in data:
        assert int(tx["fromAccountId"]) != int(tx["toAccountId"])