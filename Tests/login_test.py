#!/usr/bin/env python3
"""
login_test.py
Automated login validation using pytest and requests.
Credentials and URL are parameterized via environment variables for security.
"""
import os
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler()]
)

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.fixture(scope="session")
def login_payload():
    """Return login payload for POST request."""
    if not LOGIN_EMAIL or not LOGIN_PASSWORD:
        raise ValueError("LOGIN_EMAIL and LOGIN_PASSWORD must be set as environment variables.")
    return {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }

@pytest.mark.login
def test_login_success(login_payload):
    """
    Positive test: Expect successful login (HTTP 200 and expected response).
    """
    if not LOGIN_URL:
        pytest.skip("LOGIN_URL not set; skipping test.")
    try:
        response = requests.post(LOGIN_URL, data=login_payload, timeout=10)
        logging.info(f"POST {LOGIN_URL} -> {response.status_code}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        # Optionally, check for session token or user info in response
        assert "token" in response.json() or "session" in response.json(), "No token/session in response"
    except requests.ConnectionError as e:
        logging.error(f"Connection error: {e}")
        pytest.fail(f"Network error: {e}")
    except requests.Timeout as e:
        logging.error(f"Timeout error: {e}")
        pytest.fail(f"Timeout: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        pytest.fail(f"Unexpected error: {e}")
