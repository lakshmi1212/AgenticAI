#!/usr/bin/env python3
"""
login_test.py: Pytest-based login automation script.
Validates login functionality using environment variables for secure credential handling.
"""
import os
import pytest
import requests
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[logging.StreamHandler()]
    )

@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    setup_logging()

@pytest.mark.login
def test_login():
    url = os.getenv('LOGIN_URL')
    email = os.getenv('LOGIN_EMAIL')
    password = os.getenv('LOGIN_PASSWORD')
    assert url and email and password, 'Missing LOGIN_URL, LOGIN_EMAIL, or LOGIN_PASSWORD environment variables.'

    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        response = session.post(url, data=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        logging.error(f'Network or connection error during login: {e}')
        pytest.fail(f'Network error: {e}')

    logging.info(f'Response status: {response.status_code}')
    logging.info(f'Response URL: {response.url}')
    logging.debug(f'Response text: {response.text[:200]}')

    assert response.status_code == 200, f'Login failed: {response.text}'
    success_indicators = ['dashboard', 'success', 'logged in', 'welcome']
    assert any(ind in response.url.lower() or ind in response.text.lower() for ind in success_indicators), 'Login not successful.'

    logging.info('Login test passed successfully.')

# Usage:
#   1. Set environment variables: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
#   2. Run: pytest Tests/login_test.py --maxfail=1 --disable-warnings --tb=short --junitxml=Tests/report.xml
