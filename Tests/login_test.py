#!/usr/bin/env python3
"""
Automated login validation using pytest and requests.
Credentials are securely loaded from environment variables.
Handles network errors, authentication failures, and logs results.
"""
import os
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(
    filename="Tests/login_test.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_positive():
    """
    Positive test: Validates successful login with correct credentials.
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable not set."
    
    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
        logging.info(f"Login response: {response.status_code} {response.text}")
        assert response.status_code == 200, f"Login failed: {response.status_code}"
        # Optional: check for a token or success marker in response
        assert "token" in response.json() or "success" in response.text.lower(), "No success indicator in response."
    except requests.exceptions.Timeout:
        logging.error("Login request timed out.")
        pytest.fail("Login request timed out.")
    except requests.exceptions.ConnectionError:
        logging.error("Connection error during login.")
        pytest.fail("Connection error during login.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        pytest.fail(f"Unexpected error: {e}")
