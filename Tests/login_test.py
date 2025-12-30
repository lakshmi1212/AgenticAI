#!/usr/bin/env python3
"""
login_test.py
Automated login validation using pytest and requests.
Credentials and login URL are parameterized via environment variables for security.
Generates JUnit XML report for CI/CD integration.
"""
import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def get_credentials():
    """Fetch credentials securely from environment variables."""
    url = os.getenv('LOGIN_URL')
    email = os.getenv('LOGIN_EMAIL')
    password = os.getenv('LOGIN_PASSWORD')
    return url, email, password

@pytest.mark.parametrize('email_var, password_var, expected', [
    ('LOGIN_EMAIL', 'LOGIN_PASSWORD', True),  # Positive test
    ('LOGIN_EMAIL', 'INVALID_PASSWORD', False),  # Negative test: wrong password
])
def test_login(email_var, password_var, expected):
    """
    Test login endpoint with parameterized credentials.
    Positive and negative cases are covered.
    """
    url = os.getenv('LOGIN_URL')
    email = os.getenv(email_var)
    password = os.getenv(password_var)
    assert url and email and password, f"Missing credentials or URL (URL: {url}, Email: {email_var}, Password: {password_var})"
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        logger.info(f"Attempting login for user: {email_var}")
        response = session.post(url, data=payload, timeout=10)
    except requests.RequestException as e:
        logger.error(f"Network error during login: {e}")
        pytest.fail(f"Network error: {e}")
    logger.info(f"Response status: {response.status_code}, URL: {response.url}")
    if expected:
        assert response.status_code == 200, f"Login failed (expected success): {response.text}"
        assert ('dashboard' in response.url or 'success' in response.text.lower()), "Login not successful (expected success)."
    else:
        assert response.status_code != 200 or 'error' in response.text.lower(), "Login succeeded (expected failure)."

if __name__ == '__main__':
    pytest.main([__file__, '--junitxml=login_test_results.xml'])
