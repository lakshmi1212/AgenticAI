#!/usr/bin/env python3
"""
Automated Login Validation Script
--------------------------------
This script uses pytest and requests to validate login functionality for a web application.
Credentials and endpoint are securely loaded from environment variables.

Required Environment Variables:
    LOGIN_URL        : The login endpoint URL
    LOGIN_EMAIL      : The email/username for authentication
    LOGIN_PASSWORD   : The password for authentication

Usage:
    pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml

Troubleshooting:
    - Ensure all required environment variables are set.
    - Network errors will be logged and reported as test failures.
    - Authentication failures will report error details.
"""

import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(
    filename="Tests/login_test.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def get_env_var(key: str) -> str:
    value = os.getenv(key)
    if not value:
        logging.error(f"Missing required environment variable: {key}")
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value

@pytest.fixture(scope="module")
def login_credentials():
    return {
        "url": get_env_var("LOGIN_URL"),
        "email": get_env_var("LOGIN_EMAIL"),
        "password": get_env_var("LOGIN_PASSWORD")
    }


def test_login_positive(login_credentials):
    """
    Positive test: Validates successful login with correct credentials.
    """
    url = login_credentials["url"]
    email = login_credentials["email"]
    password = login_credentials["password"]

    payload = {
        "email": email,
        "password": password
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        logging.info(f"POST {url} with email={email}: Status {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Network error during login: {e}")
        pytest.fail(f"Network error during login: {e}")
    
    # Basic validation of login success
    assert response.status_code in [200, 201], f"Login failed: HTTP {response.status_code}"
    try:
        data = response.json()
    except Exception:
        logging.error(f"Response is not JSON: {response.text}")
        pytest.fail(f"Response is not JSON: {response.text}")
    # Check for typical success indicators (customize as needed)
    assert any(k in data for k in ["token", "access", "success", "session"]), f"Login response missing success indicator: {data}"
    logging.info("Login test passed successfully.")
