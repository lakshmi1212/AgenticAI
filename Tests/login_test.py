#!/usr/bin/env python3
"""
Pytest-based login automation test
- Uses requests for HTTP interactions
- Credentials and login URL are parameterized via environment variables
- Robust error handling and logging
"""
import os
import pytest
import requests
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("login_test")

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_success():
    """Test successful login with valid credentials."""
    assert LOGIN_URL, "LOGIN_URL env variable must be set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL env variable must be set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD env variable must be set."
    try:
        payload = {"email": LOGIN_EMAIL, "password": LOGIN_PASSWORD}
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
        logger.info(f"POST {LOGIN_URL} => status {response.status_code}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        # Optional: Validate response content for login success indication
        # For example, check for a token or success message
        assert "token" in response.json() or "success" in response.text.lower(), "Login response missing expected success indicator."
    except requests.exceptions.RequestException as e:
        logger.error(f"Network or request error: {e}")
        pytest.fail(f"Login request failed: {e}")
    except Exception as ex:
        logger.error(f"Unexpected error: {ex}")
        pytest.fail(f"Unexpected error during login: {ex}")
