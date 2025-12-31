#!/usr/bin/env python3
"""
Automated login validation test using pytest and requests.
Credentials and URL are parameterized via environment variables for security.

Required env vars:
  - LOGIN_URL
  - LOGIN_EMAIL
  - LOGIN_PASSWORD

Usage:
  $ export LOGIN_URL=https://example.com/login
  $ export LOGIN_EMAIL=your@email.com
  $ export LOGIN_PASSWORD=yourpassword
  $ pytest Tests/login_test.py --junitxml=report.xml

Returns detailed assertion errors and logs for troubleshooting.
"""
import os
import logging
import pytest
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger("login_test")

@pytest.mark.parametrize("email,password", [(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"))])
def test_login(email, password):
    """
    Test login functionality with provided credentials.
    Checks for HTTP 200 and expected success indicators in response.
    Handles common network and authentication errors.
    """
    url = os.getenv("LOGIN_URL")
    assert url, "LOGIN_URL environment variable not set."
    assert email, "LOGIN_EMAIL environment variable not set."
    assert password, "LOGIN_PASSWORD environment variable not set."
    session = requests.Session()
    payload = {"email": email, "password": password}
    try:
        logger.info(f"Attempting login to {url} as {email}")
        response = session.post(url, data=payload, timeout=10)
    except requests.RequestException as e:
        logger.error(f"Network or connection error: {e}")
        pytest.fail(f"Network or connection error: {e}")
    logger.info(f"Received status code: {response.status_code}")
    assert response.status_code == 200, f"Login failed: HTTP {response.status_code} - {response.text}"
    # Check for known success indicators (customize as needed)
    success = any([
        "dashboard" in response.url.lower(),
        "success" in response.text.lower(),
        "welcome" in response.text.lower()
    ])
    logger.info(f"Response URL: {response.url}")
    logger.debug(f"Response text: {response.text[:200]}")
    assert success, "Login not successful - success indicator not found."

def test_login_invalid_credentials():
    """
    Negative test: login with invalid credentials should fail.
    """
    url = os.getenv("LOGIN_URL")
    assert url, "LOGIN_URL environment variable not set."
    session = requests.Session()
    payload = {"email": "invalid@example.com", "password": "wrongpassword"}
    try:
        logger.info(f"Attempting login with invalid credentials to {url}")
        response = session.post(url, data=payload, timeout=10)
    except requests.RequestException as e:
        logger.error(f"Network or connection error: {e}")
        pytest.fail(f"Network or connection error: {e}")
    logger.info(f"Received status code: {response.status_code}")
    assert response.status_code in [400, 401, 403], (
        f"Expected authentication error, got HTTP {response.status_code}: {response.text}")
    # Optionally check for error message in response
    assert any([
        "invalid" in response.text.lower(),
        "error" in response.text.lower(),
        "unauthorized" in response.text.lower()
    ]), "Expected error message not found in response."
