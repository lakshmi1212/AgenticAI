#!/usr/bin/env python3
"""
Login Automation Test using Pytest
----------------------------------
- Secure credential management via environment variables
- Robust error handling and logging
- Test result reporting (JUnit XML)
"""
import os
import pytest
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@pytest.mark.parametrize("test_case", [
    {"desc": "Valid credentials", "expect_success": True},
    {"desc": "Invalid credentials", "expect_success": False}
])
def test_login(test_case):
    """
    Test login endpoint with positive and negative cases.
    Env vars required: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
    """
    url = os.getenv('LOGIN_URL')
    email = os.getenv('LOGIN_EMAIL')
    password = os.getenv('LOGIN_PASSWORD')

    assert url and email and password, "Missing LOGIN_URL, LOGIN_EMAIL, or LOGIN_PASSWORD env vars."
    session = requests.Session()
    payload = {"email": email, "password": password}
    if not test_case["expect_success"]:
        payload["password"] = "wrong_password"  # Simulate negative test

    try:
        response = session.post(url, data=payload, timeout=10)
        logging.info(f"POST {url} status={response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Network error: {e}")
        pytest.fail(f"Network error: {e}")

    if test_case["expect_success"]:
        assert response.status_code == 200, f"Login failed: {response.text}"
        assert "dashboard" in response.url or "success" in response.text.lower(), "Login not successful."
        logging.info("Login successful with valid credentials.")
    else:
        assert response.status_code != 200 or "error" in response.text.lower(), "Login should fail with invalid credentials."
        logging.info("Login failed as expected with invalid credentials.")

# Usage:
# 1. Set environment variables LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
# 2. Run: pytest login_test.py --junitxml=results.xml
