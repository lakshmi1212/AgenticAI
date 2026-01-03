"""
pytest script for automated login validation using requests.
Credentials and URL are loaded from environment variables for security.
"""
import os
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_success():
    """
    Positive test case: Valid credentials should result in successful login.
    """
    assert LOGIN_URL, "LOGIN_URL environment variable is not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable is not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable is not set."
    
    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
        logging.info(f"Login POST to {LOGIN_URL} returned status {response.status_code}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert "token" in response.json() or "success" in response.text.lower(), "Login did not return expected success indicator."
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error during login: {e}")
        pytest.fail(f"Network error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        pytest.fail(f"Unexpected error: {e}")
