#!/usr/bin/env python3
"""
Login Automation Test Script

This script uses pytest and requests for login automation. Credentials and URL are securely handled via environment variables.
Generates JUnit XML report for CI/CD integration.
"""
import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@pytest.mark.parametrize("test_case", [
    {"desc": "valid credentials", "expect_success": True},
    {"desc": "invalid password", "expect_success": False},
])
def test_login(test_case):
    url = os.getenv('LOGIN_URL')
    email = os.getenv('LOGIN_EMAIL')
    password = os.getenv('LOGIN_PASSWORD')
    assert url and email and password, 'Missing LOGIN_URL, LOGIN_EMAIL, or LOGIN_PASSWORD env vars.'
    session = requests.Session()
    payload = {'email': email, 'password': password}
    if not test_case["expect_success"]:
        payload['password'] = 'wrong_password' # Simulate negative test
    try:
        response = session.post(url, data=payload, timeout=10)
        logging.info(f"Test case: {test_case['desc']} | Status code: {response.status_code}")
        if test_case["expect_success"]:
            assert response.status_code == 200, f'Login failed: {response.text}'
            assert 'dashboard' in response.url or 'success' in response.text.lower(), 'Login not successful.'
        else:
            assert response.status_code in [401, 403, 400], f'Expected failure, got {response.status_code}'
    except requests.exceptions.RequestException as e:
        logging.error(f"Network or request error: {e}")
        pytest.fail(f"Request failed: {e}")

"""
To run:
  - Set environment variables LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
  - pytest --junitxml=report.xml login_test.py
"""
