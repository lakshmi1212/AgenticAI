#!/usr/bin/env python3
"""
Login Automation Test using pytest
- Secure credential handling (env vars)
- Robust error handling and logging
- JUnit XML reporting for CI/CD
"""
import os
import logging
import pytest
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

@pytest.mark.parametrize("email, password, expected_status", [
    (LOGIN_EMAIL, LOGIN_PASSWORD, 200),  # Positive test
    ("invalid@example.com", "wrongpass", 401),  # Negative test
])
def test_login(email, password, expected_status):
    """
    Test the login endpoint with parameterized credentials.
    Env vars required: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    session = requests.Session()
    payload = {"email": email, "password": password}
    try:
        response = session.post(LOGIN_URL, data=payload, timeout=10)
        logging.info(f"POST {LOGIN_URL} - status {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Network error: {e}")
        pytest.fail(f"Network error: {e}")
    # Check status code
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}: {response.text}"
    if expected_status == 200:
        # Success criteria: dashboard in URL or success in response
        assert ("dashboard" in response.url or "success" in response.text.lower()), "Login not successful."
    else:
        assert ("error" in response.text.lower() or "fail" in response.text.lower()), "Expected error message not found."
