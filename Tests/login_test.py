#!/usr/bin/env python3
"""
Automated login validation using pytest and requests.
Loads credentials from environment variables for secure testing.
"""
import os
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_positive():
    """
    Positive test: Valid credentials should result in successful login.
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set"
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set"
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable not set"

    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
        logging.info(f"POST {LOGIN_URL} - Status: {response.status_code}")
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        pytest.fail(f"Login request failed: {e}")

    # Success criteria: HTTP 200, and optionally, a token or success indicator in JSON
    try:
        data = response.json()
    except Exception as e:
        logging.error("Response is not valid JSON")
        pytest.fail("Login response is not JSON")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "token" in data or "success" in data, "No token or success indicator in response"
    logging.info("Login test passed.")
