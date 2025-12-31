#!/usr/bin/env python3
"""
Pytest-based login automation script.
- Reads credentials and URL from environment variables for security.
- Reports errors with detailed logging.
- Designed for CI/CD integration and robust DevOps pipelines.
"""
import os
import logging
import pytest
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@pytest.mark.parametrize("case, email, password, expected_status", [
    ("valid", os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"), 200),
    ("invalid", "invalid@example.com", "wrongpassword", 401),
])
def test_login(case, email, password, expected_status):
    """
    Test login endpoint with parameterized credentials.
    Positive and negative test cases are included.
    """
    url = os.getenv('LOGIN_URL')
    assert url, "LOGIN_URL environment variable not set."
    assert email, f"LOGIN_EMAIL environment variable not set for case: {case}"
    assert password, f"LOGIN_PASSWORD environment variable not set for case: {case}"
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        response = session.post(url, data=payload, timeout=10)
        logging.info(f"Test case: {case}, Response code: {response.status_code}, Response URL: {response.url}")
        if expected_status == 200:
            assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
            assert ("dashboard" in response.url or "success" in response.text.lower()), "Login not successful."
        else:
            assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error during login test: {e}")
        pytest.fail(f"Network error: {e}")
