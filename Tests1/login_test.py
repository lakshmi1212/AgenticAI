#!/usr/bin/env python3
"""
Login Automation Test using pytest

This script automates login validation for a web application using environment variables for credentials and endpoint.
It includes robust error handling, logging, and result reporting.
"""
import os
import pytest
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def get_env_var(name):
    value = os.getenv(name)
    if not value:
        logging.error(f"Missing environment variable: {name}")
        raise RuntimeError(f"Missing environment variable: {name}")
    return value

@pytest.mark.parametrize("email,password", [
    (os.getenv('LOGIN_EMAIL'), os.getenv('LOGIN_PASSWORD')),
    ("invalid@example.com", "wrongpassword")
])
def test_login(email, password):
    """
    Test login functionality with provided credentials.
    Positive case: Valid credentials
    Negative case: Invalid credentials
    """
    url = get_env_var('LOGIN_URL')
    assert url.startswith('http'), "LOGIN_URL must be a valid URL."
    session = requests.Session()
    payload = {"email": email, "password": password}
    try:
        response = session.post(url, data=payload, timeout=10)
        logging.info(f"POST {url} - Status: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Network error: {e}")
        pytest.fail(f"Network error: {e}")
    if email == os.getenv('LOGIN_EMAIL') and password == os.getenv('LOGIN_PASSWORD'):
        # Positive test: Expect success
        assert response.status_code == 200, f"Login failed: {response.text}"
        assert 'dashboard' in response.url or 'success' in response.text.lower(), "Login not successful."
        logging.info("Login successful.")
    else:
        # Negative test: Expect failure
        assert response.status_code in (400, 401, 403), "Expected login failure, got status: {response.status_code}"
        logging.info("Login failed as expected for invalid credentials.")

# Usage: Set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD env vars. Run: pytest login_test.py --junitxml=results.xml
