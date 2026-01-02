#!/usr/bin/env python3
"""
Automated login validation using pytest.
Credentials are sourced from environment variables for security.
Robust error handling and logging included.
"""
import os
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler()]
)

LOGIN_URL = os.environ.get('LOGIN_URL')
LOGIN_EMAIL = os.environ.get('LOGIN_EMAIL')
LOGIN_PASSWORD = os.environ.get('LOGIN_PASSWORD')

@pytest.mark.login
def test_login_positive():
    """
    Positive login test - expects successful authentication.
    """
    assert LOGIN_URL, "LOGIN_URL environment variable is not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable is not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable is not set."
    
    payload = {
        'email': LOGIN_EMAIL,
        'password': LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
        logging.info(f"POST {LOGIN_URL} with payload {payload}")
    except requests.RequestException as e:
        logging.error(f"Network error: {e}")
        pytest.fail(f"Network error during login: {e}")
    
    assert response.status_code == 200, f"Login failed: {response.status_code}, {response.text}"
    # Optionally, check for authentication token or success indicator
    if 'token' in response.json():
        logging.info("Login successful, token received.")
    elif response.json().get('success'):
        logging.info("Login successful (success=True).")
    else:
        logging.warning(f"Login response did not contain expected success indicator: {response.text}")
        pytest.fail(f"Login did not return expected success indicator: {response.text}")

if __name__ == "__main__":
    pytest.main([__file__, '--junitxml=Tests/login_test_results.xml'])
