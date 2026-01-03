#!/usr/bin/env python3
"""
Login Automation Test using pytest and requests.
Credentials and URL are provided via environment variables.
"""
import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.environ.get('LOGIN_URL')
LOGIN_EMAIL = os.environ.get('LOGIN_EMAIL')
LOGIN_PASSWORD = os.environ.get('LOGIN_PASSWORD')

@pytest.mark.login
def test_login_success():
    """Test successful login with valid credentials."""
    assert LOGIN_URL, 'LOGIN_URL environment variable not set.'
    assert LOGIN_EMAIL, 'LOGIN_EMAIL environment variable not set.'
    assert LOGIN_PASSWORD, 'LOGIN_PASSWORD environment variable not set.'

    payload = {
        'email': LOGIN_EMAIL,
        'password': LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
        logging.info(f'Request sent to {LOGIN_URL} with email {LOGIN_EMAIL}')
    except requests.RequestException as e:
        logging.error(f'Network error during login: {e}')
        pytest.fail(f'Network error: {e}')

    assert response.status_code == 200, f'Unexpected status code: {response.status_code}'
    try:
        data = response.json()
    except Exception as e:
        logging.error(f'Failed to parse JSON response: {e}')
        pytest.fail(f'Invalid JSON response: {e}')

    assert 'token' in data or data.get('success', False), 'Login failed: No token or success flag in response.'
    logging.info('Login test passed. Token or success flag found.')
