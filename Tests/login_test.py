#!/usr/bin/env python3
"""
Pytest script for login validation automation.
- Uses environment variables for credentials and URL.
- Handles network/auth errors robustly.
- Logs steps and errors.
- Produces JUnit XML/HTML reports if pytest is run with appropriate flags.
"""
import os
import logging
import pytest
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def get_env(var: str) -> str:
    val = os.getenv(var)
    if not val:
        logger.error(f"Missing required environment variable: {var}")
        pytest.skip(f"Missing required environment variable: {var}")
    return val

def login(url, email, password):
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        logger.info(f"POST {url} with user {email}")
        response = session.post(url, data=payload, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Network/Auth error: {e}")
        pytest.fail(f"Login request failed: {e}")

def test_login_success():
    """Test successful login with correct credentials."""
    url = get_env('LOGIN_URL')
    email = get_env('LOGIN_EMAIL')
    password = get_env('LOGIN_PASSWORD')
    response = login(url, email, password)
    assert response.status_code == 200, f"Login failed: {response.text}"
    assert ('dashboard' in response.url or 'success' in response.text.lower()), "Login not successful."

@pytest.mark.negative
def test_login_failure():
    """Test login with incorrect password (negative case)."""
    url = get_env('LOGIN_URL')
    email = get_env('LOGIN_EMAIL')
    bad_password = 'invalid_password!@#'
    response = login(url, email, bad_password)
    assert response.status_code in (401, 403, 400), f"Expected failure, got {response.status_code}"
    assert ("invalid" in response.text.lower() or "error" in response.text.lower() or response.status_code in (401, 403, 400)), "Expected login failure response."

# Usage: set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD as env vars. Run: pytest login_test.py --junitxml=results.xml
