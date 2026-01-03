#!/usr/bin/env python3
"""
Pytest-based login automation for validating authentication endpoint.
Uses environment variables for secure credential management.
"""
import os
import requests
import pytest

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.parametrize("login_url, email, password", [
    (LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD)
])
def test_login_success(login_url, email, password):
    """
    Test successful login with valid credentials.
    """
    assert login_url, "LOGIN_URL environment variable must be set."
    assert email, "LOGIN_EMAIL environment variable must be set."
    assert password, "LOGIN_PASSWORD environment variable must be set."
    try:
        response = requests.post(
            login_url,
            json={"email": email, "password": password},
            timeout=10
        )
    except requests.exceptions.RequestException as exc:
        pytest.fail(f"Network error during login request: {exc}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    # Optionally validate response content (e.g., presence of token, user info)
    data = response.json()
    assert "token" in data or "access_token" in data, "No token found in response."

@pytest.mark.parametrize("login_url, email, password", [
    (LOGIN_URL, LOGIN_EMAIL, "wrongpassword")
])
def test_login_failure(login_url, email, password):
    """
    Test failed login with invalid password.
    """
    assert login_url, "LOGIN_URL environment variable must be set."
    assert email, "LOGIN_EMAIL environment variable must be set."
    try:
        response = requests.post(
            login_url,
            json={"email": email, "password": password},
            timeout=10
        )
    except requests.exceptions.RequestException as exc:
        pytest.fail(f"Network error during login request: {exc}")
    assert response.status_code in [400, 401, 403], f"Expected failure status, got {response.status_code}. Response: {response.text}"
