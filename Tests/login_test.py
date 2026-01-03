#!/usr/bin/env python3
"""
Automated login validation using pytest and requests
Credentials and login URL are loaded securely from environment variables
"""
import os
import pytest
import requests

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login():
    assert LOGIN_URL, "LOGIN_URL not set in environment variables"
    assert LOGIN_EMAIL, "LOGIN_EMAIL not set in environment variables"
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD not set in environment variables"
    
    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, data=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network error during login request: {e}")
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    try:
        data = response.json()
    except Exception:
        pytest.fail("Response not in JSON format")
    
    # Success criteria: JSON contains a token or authenticated indicator
    assert "token" in data or "authenticated" in data, "Login response missing expected fields"
    assert data.get("authenticated", True) or data.get("token"), "Login failed: No token or authenticated flag received"
