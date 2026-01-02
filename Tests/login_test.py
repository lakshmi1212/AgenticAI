#!/usr/bin/env python3
"""
Pytest script for automated login validation.
- Reads credentials and URL from environment variables.
- Validates both successful and failed login attempts.
- Uses requests library for HTTP interactions.
- Robust error handling, logging, and reporting.
"""
import os
import pytest
import requests
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
INVALID_PASSWORD = os.getenv('INVALID_PASSWORD')

@pytest.mark.parametrize('email,password,expected_status', [
    (LOGIN_EMAIL, LOGIN_PASSWORD, 'success'),
    (LOGIN_EMAIL, INVALID_PASSWORD, 'failure'),
])
def test_login(email, password, expected_status):
    """
    Attempts login and asserts outcome based on credentials.
    """
    assert LOGIN_URL, "LOGIN_URL environment variable not set!"
    assert email, "LOGIN_EMAIL environment variable not set!"
    assert password, "LOGIN_PASSWORD or INVALID_PASSWORD not set!"
    
    try:
        # Example payload - adjust according to actual login API
        payload = {
            'email': email,
            'password': password
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(LOGIN_URL, json=payload, headers=headers, timeout=10)
        logging.info(f"Login attempt for {email}: {response.status_code} {response.text}")
        if expected_status == 'success':
            assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
            assert 'token' in response.json() or 'access' in response.json(), "No auth token found in response."
        else:
            assert response.status_code in [400, 401, 403], f"Expected authentication failure, got {response.status_code}"
    except requests.exceptions.RequestException as e:
        logging.error(f"Network or HTTP error: {e}")
        pytest.fail(f"Network or HTTP error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        pytest.fail(f"Unexpected error: {e}")
