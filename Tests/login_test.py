#!/usr/bin/env python3
"""
Automated login validation using pytest & requests.
Credentials are loaded securely from environment variables.
"""
import os
import requests
import pytest

LOGIN_URL = os.environ.get("LOGIN_URL")
LOGIN_EMAIL = os.environ.get("LOGIN_EMAIL")
LOGIN_PASSWORD = os.environ.get("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_success():
    """Test successful login with valid credentials."""
    assert LOGIN_URL, "LOGIN_URL env var not set"
    assert LOGIN_EMAIL, "LOGIN_EMAIL env var not set"
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD env var not set"

    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    json_resp = response.json() if response.headers.get('content-type', '').startswith('application/json') else {}
    assert json_resp.get("success") is True or "token" in json_resp, "Login failed or token missing in response"

@pytest.mark.login
def test_login_failure():
    """Test failed login with invalid credentials."""
    assert LOGIN_URL, "LOGIN_URL env var not set"
    payload = {
        "email": "wrong@example.com",
        "password": "wrongpassword"
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code in [400, 401, 403], f"Expected auth failure, got {response.status_code}"
    json_resp = response.json() if response.headers.get('content-type', '').startswith('application/json') else {}
    assert json_resp.get("success") is False or "error" in json_resp, "Expected failure response"
