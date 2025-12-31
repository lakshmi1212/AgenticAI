#!/usr/bin/env python3
"""
login_test.py
Automated login validation using pytest and requests with secure credential handling.
"""
import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("case, email, password, expected_status", [
    ("positive", os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"), 200),
    ("negative_wrong_password", os.getenv("LOGIN_EMAIL"), "invalid_password", 401),
])
def test_login(case, email, password, expected_status):
    """
    Validates login functionality with positive and negative test cases.
    Credentials are provided via environment variables for security.
    """
    url = os.getenv("LOGIN_URL")
    assert url, "LOGIN_URL environment variable not set."
    assert email, "LOGIN_EMAIL environment variable not set."
    assert password, "LOGIN_PASSWORD environment variable not set (for positive test)."

    session = requests.Session()
    payload = {"email": email, "password": password}
    try:
        response = session.post(url, data=payload, timeout=10)
        logger.info(f"Test case: {case}, POST {url}, status: {response.status_code}")
    except requests.RequestException as e:
        logger.error(f"Network error during login POST: {e}")
        pytest.fail(f"Network error during login POST: {e}")

    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}: {response.text}"
    if case == "positive":
        # Basic success validation
        assert ("dashboard" in response.url or "success" in response.text.lower()), "Login not successful."
    else:
        # Negative case: error message or redirect
        assert ("invalid" in response.text.lower() or "error" in response.text.lower()), "Expected failure message missing."

    logger.info(f"Test {case} completed successfully.")
