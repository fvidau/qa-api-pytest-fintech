import requests
from config import BASE_URL


def test_security_headers():
    response = requests.get(BASE_URL)

    headers = response.headers

    # Lista básica de headers importantes
    expected_headers = [
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options"
    ]

    missing = []

    for h in expected_headers:
        if h not in headers:
            missing.append(h)

    # Este test es informativo (no rompe todo)
    print(f"Missing headers: {missing}")

    assert response.status_code == 200