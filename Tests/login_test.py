#!/usr/bin/env python3
"""
Pytest login automation for validating authentication with positive and negative test cases.
Credentials are loaded from environment variables for security.
"""
import os
import requests
import pytest

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")

@pytest.fixture(scope="module")
def session():
    return requests.Session()

@pytest.mark.parametrize("password,is_valid", [
    (LOGIN_PASSWORD, True),
    (INVALID_PASSWORD, False)
])
def test_login(session, password, is_valid):
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    assert password, "Password parameter not set."
    payload = {
        "email": LOGIN_EMAIL,
        "password": password
    }
    try:
        response = session.post(LOGIN_URL, json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code in (200, 401, 400), f"Unexpected HTTP status code: {response.status_code}"
    if is_valid:
        assert response.status_code == 200, f"Expected successful login, got {response.status_code}"
        assert "token" in response.json() or "auth" in response.json(), "No authentication token found in response."
    else:
        assert response.status_code in (401, 400), f"Expected authentication failure, got {response.status_code}"
        assert "error" in response.json() or "message" in response.json(), "No error message in failed login response."
