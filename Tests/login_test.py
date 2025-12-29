#!/usr/bin/env python3
"""
login_test.py
Automated login validation using pytest and requests.
Credentials and login URL must be provided via environment variables for security.
Generates JUnit XML test report for CI/CD integration.
"""
import os
import logging
import pytest
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("email,password,expected", [
    # Positive test (correct credentials)
    (os.getenv('LOGIN_EMAIL'), os.getenv('LOGIN_PASSWORD'), True),
    # Negative test (wrong password)
    (os.getenv('LOGIN_EMAIL'), 'invalid_password', False),
])
def test_login(email, password, expected):
    """
    Test login functionality with positive and negative scenarios.
    Expects environment variables: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
    """
    url = os.getenv('LOGIN_URL')
    assert url, 'LOGIN_URL not set in environment.'
    assert email, 'LOGIN_EMAIL not set in environment.'
    assert password is not None, 'LOGIN_PASSWORD not set in environment.'

    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        response = session.post(url, data=payload, timeout=10)
        logger.info(f'POST {url} -> {response.status_code}')
    except requests.RequestException as e:
        logger.error(f'Network error: {e}')
        pytest.fail(f'Network error: {e}')

    if expected:
        assert response.status_code == 200, f'Login failed: {response.text}'
        assert ("dashboard" in response.url or "success" in response.text.lower()), "Login not successful."
    else:
        assert response.status_code in (401, 403, 400) or "invalid" in response.text.lower(), "Negative login did not fail as expected."

    logger.info(f'Login test (expected={expected}) completed.')

# Usage:
#   Set environment variables: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
#   Run tests: pytest --junitxml=results.xml login_test.py
