import os
import requests
import pytest

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_success():
    """
    Test login endpoint with valid credentials.
    Environment variables required:
      - LOGIN_URL
      - LOGIN_EMAIL
      - LOGIN_PASSWORD
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable not set."
    
    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    
    # Success: 2xx status code and typically some token in the response
    assert response.status_code == 200, f"Login failed with status {response.status_code}: {response.text}"
    data = response.json()
    assert "token" in data or "access_token" in data, "No token found in login response."

@pytest.mark.login
def test_login_invalid_password():
    """
    Test login endpoint with invalid password.
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    wrong_password = "invalid_password_123!"
    payload = {
        "email": LOGIN_EMAIL,
        "password": wrong_password
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code in [401, 403], f"Expected failure, got status {response.status_code}: {response.text}"
