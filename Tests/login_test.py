#!/usr/bin/env python3
"""
Pytest login automation using requests. Credentials and login URL are provided via environment variables.
Robust error handling and logging are included.
"""
import os
import requests
import pytest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

@pytest.fixture(scope='module')
def login_payload():
    assert LOGIN_URL, 'LOGIN_URL environment variable not set.'
    assert LOGIN_EMAIL, 'LOGIN_EMAIL environment variable not set.'
    assert LOGIN_PASSWORD, 'LOGIN_PASSWORD environment variable not set.'
    return {
        'url': LOGIN_URL,
        'data': {
            'email': LOGIN_EMAIL,
            'password': LOGIN_PASSWORD
        }
    }

@pytest.mark.login
def test_login_positive(login_payload):
    """
    Positive test case: Valid login credentials should result in successful authentication.
    """
    try:
        response = requests.post(login_payload['url'], json=login_payload['data'], timeout=10)
        logging.info(f'Response status code: {response.status_code}')
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        # Optional: check for authentication token or success message
        resp_json = response.json()
        assert 'token' in resp_json or 'success' in response.text.lower(), "Login response missing expected success indicator."
    except requests.exceptions.Timeout:
        logging.error('Login request timed out.')
        pytest.fail('Login request timed out.')
    except requests.exceptions.ConnectionError as ce:
        logging.error(f'Connection error: {ce}')
        pytest.fail(f'Connection error: {ce}')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        pytest.fail(f'Unexpected error: {e}')
