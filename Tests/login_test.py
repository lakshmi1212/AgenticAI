#!/usr/bin/env python3
"""
Automated login test using pytest and requests.
Credentials and URL are read from environment variables for security.
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
    Positive test: Validates successful login with correct credentials.
    """
    assert LOGIN_URL, "LOGIN_URL environment variable is not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable is not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable is not set."
    try:
        response = requests.post(LOGIN_URL, json={
            "email": LOGIN_EMAIL,
            "password": LOGIN_PASSWORD
        }, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    try:
        data = response.json()
    except Exception:
        pytest.fail(f"Response is not valid JSON: {response.text}")
    assert "token" in data or "session" in data or data.get("success", False), "Login response missing expected authentication information."
