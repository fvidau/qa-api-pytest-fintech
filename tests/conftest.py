import pytest
import requests
from config import BASE_URL


@pytest.fixture
def get_transactions():
    return requests.get(f"{BASE_URL}/transactions")


@pytest.fixture
def get_accounts():
    return requests.get(f"{BASE_URL}/accounts")


# 🔥 NUEVO (para negativos)
@pytest.fixture
def get_invalid():
    return requests.get(f"{BASE_URL}/invalid")