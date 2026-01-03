#!/usr/bin/env python3
"""
Pytest automated login validation using requests.
Credentials and URL are provided via environment variables for security.
"""
import os
import pytest
import requests

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.parametrize("email,password", [(LOGIN_EMAIL, LOGIN_PASSWORD)])
def test_login_success(email, password):
    assert LOGIN_URL, "LOGIN_URL env variable not set."
    assert email, "LOGIN_EMAIL env variable not set."
    assert password, "LOGIN_PASSWORD env variable not set."
    
    payload = {
        "email": email,
        "password": password
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network error during login request: {e}")
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    json_data = response.json() if response.headers.get("content-type","").startswith("application/json") else None
    assert json_data is not None, "Response is not valid JSON."
    assert "token" in json_data or "access_token" in json_data, "Login response missing authentication token."
    
    # Additional checks can be added for 2FA, CSRF tokens etc. if present in response.
    # Logging for debug:
    print(f"Login response JSON: {json_data}")
