#!/usr/bin/env python3
"""
Login Automation Test using pytest
Author: Senior QA Automation Engineer

This script validates login functionality for a web application.
Credentials and login URL are securely loaded from environment variables.

Test Cases:
 1. Successful login with valid credentials
 2. Unsuccessful login with invalid password

Usage:
 - Set environment variables: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD, INVALID_PASSWORD
 - Run: pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml

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
    """Create a requests session for persistent cookies."""
    return requests.Session()

def login(session, email, password):
    """Attempt login and return response."""
    if not LOGIN_URL:
        raise ValueError("LOGIN_URL environment variable not set.")
    payload = {
        "email": email,
        "password": password
    }
    try:
        resp = session.post(LOGIN_URL, data=payload, timeout=10)
        resp.raise_for_status()
        return resp
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network or HTTP error during login: {e}")

@pytest.mark.parametrize("email,password,expected", [
    (LOGIN_EMAIL, LOGIN_PASSWORD, True),
    (LOGIN_EMAIL, INVALID_PASSWORD, False)
])
def test_login(session, email, password, expected):
    """
    Test login with given credentials.
    Checks for successful or failed authentication.
    """
    resp = login(session, email, password)
    # Example logic: success if status code == 200 and 'token' in JSON response
    try:
        data = resp.json()
    except ValueError:
        pytest.fail("Response was not valid JSON.")
    if expected:
        assert resp.status_code == 200, f"Expected 200 OK, got {resp.status_code}"
        assert "token" in data, "Expected authentication token in response."
    else:
        assert resp.status_code in [401, 403], f"Expected 401/403 for invalid login, got {resp.status_code}"
        assert "error" in data or "message" in data, "Expected error message for failed login."
