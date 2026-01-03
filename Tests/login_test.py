#!/usr/bin/env python3
"""
Automated login validation using pytest and requests.
Credentials are read from environment variables for security.
"""
import os
import pytest
import requests

LOGIN_URL = os.environ.get('LOGIN_URL')
LOGIN_EMAIL = os.environ.get('LOGIN_EMAIL')
LOGIN_PASSWORD = os.environ.get('LOGIN_PASSWORD')

@pytest.mark.login
def test_login_success():
    """Test login with valid credentials."""
    assert LOGIN_URL, "LOGIN_URL environment variable is not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable is not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable is not set."
    
    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login request: {e}")
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    # Assuming successful login returns a token or success message
    assert "token" in response.json() or "success" in response.text.lower(), "Login failed: No token or success message in response."

@pytest.mark.login
def test_login_failure():
    """Test login with invalid credentials."""
    assert LOGIN_URL, "LOGIN_URL environment variable is not set."
    payload = {
        "email": "invalid@example.com",
        "password": "wrongpassword"
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login request: {e}")
    
    assert response.status_code in [400, 401, 403], f"Expected authentication failure status, got {response.status_code}"
    assert "error" in response.text.lower() or "invalid" in response.text.lower(), "Expected error message in response for failed login."
