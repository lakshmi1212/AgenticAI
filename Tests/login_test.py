#!/usr/bin/env python3
"""
Pytest-based login validation script for automated authentication testing.
Credentials and login URL must be provided via environment variables for security:
  - LOGIN_URL
  - LOGIN_EMAIL
  - LOGIN_PASSWORD

Test results are reported in standard pytest format (supports JUnit XML, HTML plugins).
"""
import os
import pytest
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

@pytest.fixture(scope="module")
def credentials():
    url = os.getenv('LOGIN_URL')
    email = os.getenv('LOGIN_EMAIL')
    password = os.getenv('LOGIN_PASSWORD')
    assert url, "LOGIN_URL environment variable must be set."
    assert email, "LOGIN_EMAIL environment variable must be set."
    assert password, "LOGIN_PASSWORD environment variable must be set."
    return url, email, password

@pytest.mark.parametrize("email,password,expected_status", [
    (os.getenv('LOGIN_EMAIL'), os.getenv('LOGIN_PASSWORD'), 200),  # Positive case
    ("wrong@example.com", "wrongpassword", 401),                # Negative case
])
def test_login(credentials, email, password, expected_status):
    url, _, _ = credentials
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        logging.info(f"Attempting login to {url} with user {email}")
        response = session.post(url, data=payload, timeout=10)
    except requests.RequestException as e:
        logging.error(f"Network or connection error: {e}")
        pytest.fail(f"Network error during login: {e}")
    logging.info(f"Response status: {response.status_code}")
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}. Response: {response.text}"
    if expected_status == 200:
        assert ("dashboard" in response.url.lower() or "success" in response.text.lower()), "Login did not reach dashboard or indicate success."
    else:
        assert ("error" in response.text.lower() or response.status_code != 200), "Negative login did not return error as expected."
