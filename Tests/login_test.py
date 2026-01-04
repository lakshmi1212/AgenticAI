#!/usr/bin/env python3
"""
Pytest script for automated login validation using requests.
Credentials and login URL are read from environment variables for security.
"""
import os
import pytest
import requests

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_success():
    """
    Positive test: Verify login with correct credentials
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable not set."
    try:
        response = requests.post(
            LOGIN_URL,
            json={"email": LOGIN_EMAIL, "password": LOGIN_PASSWORD},
            timeout=10
        )
    except requests.RequestException as e:
        pytest.fail(f"Network or request error: {e}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    json_data = response.json()
    assert "token" in json_data or "access_token" in json_data, "Login response missing token."
    assert json_data.get("token") or json_data.get("access_token"), "Token value missing in response."

@pytest.mark.login
@pytest.mark.parametrize("email,password", [
    ("wrong@example.com", "wrongpass"),
    (LOGIN_EMAIL, "wrongpass"),
    ("", ""),
])
def test_login_failure(email, password):
    """
    Negative test: Verify login fails with invalid credentials
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    try:
        response = requests.post(
            LOGIN_URL,
            json={"email": email, "password": password},
            timeout=10
        )
    except requests.RequestException as e:
        pytest.fail(f"Network or request error: {e}")
    assert response.status_code in [400, 401, 403], f"Expected 400/401/403, got {response.status_code}"
    json_data = response.json()
    assert "error" in json_data or "message" in json_data, "Error message missing in response."
