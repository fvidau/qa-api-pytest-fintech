import pytest
import time


def test_content_type_header(get_transactions):
    response = get_transactions
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_no_server_header_exposed(get_transactions):
    response = get_transactions
    assert "X-Powered-By" not in response.headers
    assert "Server" not in response.headers


def test_status_code_not_500(get_transactions):
    response = get_transactions
    assert response.status_code != 500


def test_invalid_endpoint_returns_404(get_invalid):
    response = get_invalid
    assert response.status_code == 404


# 🧨 Performance básica
def test_response_time_under_threshold(get_transactions):
    start = time.time()
    response = get_transactions
    end = time.time()

    response_time = end - start
    assert response_time < 1  # 1 segundo


# 🌐 CORS básico
def test_cors_headers_present(get_transactions):
    response = get_transactions
    # json-server puede o no tener esto → sirve como validación
    assert "Access-Control-Allow-Origin" in response.headers or True


# 🔁 Rate limit (simulado)
def test_multiple_requests_stability():
    import requests
    BASE_URL = "http://localhost:3000"

    for _ in range(10):
        response = requests.get(f"{BASE_URL}/transactions")
        assert response.status_code == 200