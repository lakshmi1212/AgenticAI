#!/usr/bin/env python3
"""
pytest script for automated login validation using requests.
Credentials are securely loaded from environment variables.
"""
import os
import pytest
import requests

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

def is_configured():
    return all([LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD])

def login_request(url, email, password):
    try:
        response = requests.post(
            url,
            json={"email": email, "password": password},
            timeout=10
        )
        return response
    except requests.RequestException as e:
        pytest.fail(f"Network or request error: {e}")

@pytest.mark.skipif(not is_configured(), reason="Environment variables for login not set.")
def test_login_success():
    """
    Positive test: Ensure login succeeds with correct credentials.
    """
    resp = login_request(LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD)
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    assert "token" in resp.json() or "access" in resp.json(), "Login response missing expected auth token."
    # Additional checks: e.g., session, cookies, etc.

@pytest.mark.parametrize("email,password,expected_status", [
    ("wrong@example.com", "wrongpass", 401),
    ("", LOGIN_PASSWORD, 400),
    (LOGIN_EMAIL, "", 400)
])
def test_login_negative(email, password, expected_status):
    """
    Negative tests: Incorrect credentials, missing fields.
    """
    resp = login_request(LOGIN_URL, email, password)
    assert resp.status_code == expected_status, f"Expected {expected_status}, got {resp.status_code}"
