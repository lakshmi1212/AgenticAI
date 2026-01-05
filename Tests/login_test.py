"""
pytest-based login automation script using requests.
Credentials and login URL are sourced from environment variables for security.
Handles success, authentication failure, and network errors.
"""
import os
import pytest
import requests

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.fixture(scope="module")
def login_payload():
    assert LOGIN_URL, "LOGIN_URL environment variable must be set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable must be set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable must be set."
    return {
        "url": LOGIN_URL,
        "data": {
            "email": LOGIN_EMAIL,
            "password": LOGIN_PASSWORD
        }
    }

def test_login_success(login_payload):
    """
    Positive test: Validates successful login.
    """
    try:
        response = requests.post(login_payload["url"], json=login_payload["data"], timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code} - {response.text}"
    # Optional: Validate a token or specific response field
    json_data = response.json()
    assert "token" in json_data or "success" in json_data, "Login response missing expected keys."

def test_login_failure_wrong_password(login_payload):
    """
    Negative test: Invalid password should not allow login.
    """
    invalid_data = login_payload["data"].copy()
    invalid_data["password"] = "wrong_password_123"
    try:
        response = requests.post(login_payload["url"], json=invalid_data, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code in [400, 401, 403], f"Expected authentication failure, got {response.status_code} - {response.text}"
    json_data = response.json()
    assert "error" in json_data or "message" in json_data, "Expected error message in response."
