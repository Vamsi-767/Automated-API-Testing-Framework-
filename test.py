import pytest
import requests

BASE_URL = "http://localhost:5001"

API_ENDPOINTS = [
    {"endpoint": "/ping", "method": "GET", "expected_status": 200},
    {"endpoint": "/pinging", "method": "GET", "expected_status": 200},
    {"endpoint": "/echo", "method": "POST", "expected_status": 200, "payload": {"hello": "world"}},
    {"endpoint": "/status/200", "method": "GET", "expected_status": 200},
    {"endpoint": "/status/404", "method": "GET", "expected_status": 404},
]

@pytest.mark.parametrize("api", API_ENDPOINTS)
def test_api_status_code(api):
    url = BASE_URL + api["endpoint"]
    method = api["method"].upper()

    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, json=api.get("payload", {}))
    elif method == "PUT":
        response = requests.put(url, json=api.get("payload", {}))
    elif method == "DELETE":
        response = requests.delete(url)
    else:
        pytest.fail(f"Unsupported HTTP method: {method}")

    assert response.status_code == api["expected_status"], (
        f"Expected {api['expected_status']}, but got {response.status_code} for {method} {url}"
    )
