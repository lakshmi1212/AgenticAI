#!/usr/bin/env python3
"""
Automated login validation using pytest and requests.
Credentials are securely loaded from environment variables for CI/CD compatibility.
"""
import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

def is_env_set():
    missing = [v for v, val in zip([
        "LOGIN_URL", "LOGIN_EMAIL", "LOGIN_PASSWORD"], [LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD]) if not val]
    if missing:
        logger.error(f"Missing environment variables: {', '.join(missing)}")
        return False
    return True

@pytest.mark.login
def test_login_success():
    """
    Test for successful login.
    Assumes the login API accepts POST with 'email' and 'password'.
    """
    assert is_env_set(), "Required environment variables are not set."

    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
        logger.info(f"POST {LOGIN_URL} returned status {response.status_code}")
    except requests.RequestException as e:
        logger.error(f"Network or request error: {e}")
        pytest.fail(f"Login request failed: {e}")

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    try:
        resp_json = response.json()
    except Exception:
        logger.error("Response is not valid JSON.")
        pytest.fail("Response is not valid JSON.")

    # Success criteria: token or success field in response
    assert "token" in resp_json or resp_json.get("success", False), "Login failed or token not found in response."
    logger.info("Login test passed.")

if __name__ == "__main__":
    pytest.main([__file__, "--junitxml=Tests/login_test_results.xml"])
