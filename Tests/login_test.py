#!/usr/bin/env python3
"""
Automated login validation using pytest and requests.
- Credentials and login URL are sourced securely from environment variables.
- Robust error handling for network/authentication failures.
- Logs results for troubleshooting.
"""
import os
import pytest
import requests
import logging

def get_env_var(name):
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Missing required environment variable: {name}")
    return value

@pytest.mark.login
def test_login():
    url = get_env_var('LOGIN_URL')
    email = get_env_var('LOGIN_EMAIL')
    password = get_env_var('LOGIN_PASSWORD')
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        response = session.post(url, data=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error during login: {e}")
        pytest.fail(f"Network error: {e}")
    assert response.status_code == 200, f"Login failed (HTTP {response.status_code}): {response.text}" 
    # Check for successful login indication (customize as needed)
    if 'dashboard' not in response.url and 'success' not in response.text.lower():
        logging.error(f"Login response did not indicate success. URL: {response.url}, Body: {response.text}")
        pytest.fail("Login not successful.")
    logging.info(f"Login successful for {email} at {url}")

# Usage:
# 1. Set environment variables LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD.
# 2. Run: pytest Tests/login_test.py --maxfail=1 --disable-warnings --junitxml=login_test_results.xml
