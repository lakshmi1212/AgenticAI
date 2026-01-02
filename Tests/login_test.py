#!/usr/bin/env python3
"""
pytest script for automated login validation.

Usage:
  - Set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD as environment variables.
  - Run: pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
"""
import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

@pytest.mark.login
def test_login_success():
    """
    Positive test case: Attempt login with valid credentials.
    """
    assert LOGIN_URL, 'LOGIN_URL environment variable not set.'
    assert LOGIN_EMAIL, 'LOGIN_EMAIL environment variable not set.'
    assert LOGIN_PASSWORD, 'LOGIN_PASSWORD environment variable not set.'
    
    payload = {
        'email': LOGIN_EMAIL,
        'password': LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, data=payload, timeout=10)
        logging.info(f'Login POST to {LOGIN_URL} responded with status {response.status_code}')
        assert response.status_code == 200, f"Login failed, status: {response.status_code}"
        # Check for successful login indicator (customize as needed)
        assert 'success' in response.text.lower() or response.json().get('authenticated', False), 'Login response did not indicate success.'
    except requests.exceptions.RequestException as e:
        logging.error(f'Network or request error: {e}')
        pytest.fail(f'RequestException: {e}')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        pytest.fail(f'Unexpected error: {e}')

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '--junitxml=Tests/login_test_results.xml']))
