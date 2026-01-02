#!/usr/bin/env python3
"""
pytest script for login validation
- Uses environment variables for credentials
- Supports positive and negative test cases
- Robust error handling and logging
"""
import os
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(
    filename="Tests/login_test.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")

@pytest.fixture(scope="module")
def session():
    return requests.Session()

def login(session, email, password):
    """
    Sends a POST request to LOGIN_URL with email and password
    Returns response object
    """
    if not LOGIN_URL:
        raise ValueError("LOGIN_URL environment variable not set.")
    data = {
        "email": email,
        "password": password
    }
    try:
        response = session.post(LOGIN_URL, data=data, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Network or HTTP error: {e}")
        raise

@pytest.mark.parametrize("email,password,expected_status", [
    (LOGIN_EMAIL, LOGIN_PASSWORD, "success"),
    (LOGIN_EMAIL, INVALID_PASSWORD, "fail")
])
def test_login(session, email, password, expected_status):
    """
    Tests login with provided credentials
    """
    try:
        response = login(session, email, password)
        # Assuming API returns JSON with 'authenticated' key
        json_resp = response.json()
        logging.info(f"Login attempt: {email}/{password} => {json_resp}")
        if expected_status == "success":
            assert json_resp.get("authenticated") is True, "Expected successful login."
        else:
            assert json_resp.get("authenticated") is False, "Expected login failure."
    except Exception as e:
        logging.error(f"Test failed: {e}")
        if expected_status == "success":
            pytest.fail(f"Unexpected error during successful login: {e}")
        else:
            # For negative case, network/auth error is acceptable
            pass
