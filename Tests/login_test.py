#!/usr/bin/env python3
"""
Login Automation Test using pytest and requests
- Credentials and URL are parameterized via environment variables for security
- Robust error handling and logging included
- Designed for DevOps integration and maintainability
"""
import os
import logging
import pytest
import requests
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

def is_login_successful(response):
    """
    Custom logic to determine if login was successful
    Adjust as needed for target application (e.g., dashboard in URL, token in body, etc.)
    """
    if response.status_code == 200:
        if 'dashboard' in response.url or 'success' in response.text.lower():
            return True
    return False

@pytest.mark.login
@pytest.mark.parametrize("email,password,expected", [
    (LOGIN_EMAIL, LOGIN_PASSWORD, True),  # Positive test
    ("wrong@example.com", "wrongpass", False),  # Negative test
])
def test_login(email, password, expected):
    assert LOGIN_URL, 'LOGIN_URL not set in environment.'
    assert email, 'LOGIN_EMAIL not set.'
    assert password, 'LOGIN_PASSWORD not set.'
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        logging.info(f"Attempting login for {email} at {LOGIN_URL}")
        response = session.post(LOGIN_URL, data=payload, timeout=10)
        logging.info(f"Login response code: {response.status_code}")
    except RequestException as e:
        logging.error(f"Network error during login: {e}")
        pytest.fail(f"Network error: {e}")
    if expected:
        assert is_login_successful(response), f"Login failed for valid credentials: {response.text}"
    else:
        assert not is_login_successful(response), "Login succeeded with invalid credentials, which is a security risk."
