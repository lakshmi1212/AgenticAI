#!/usr/bin/env python3
"""
Automated login validation using pytest.
Credentials and endpoint are sourced from environment variables for security.
Generates JUnit XML report for integration with CI/CD pipelines.
"""
import os
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger("login_test")

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

def is_env_configured():
    missing = []
    for var in ["LOGIN_URL", "LOGIN_EMAIL", "LOGIN_PASSWORD"]:
        if not os.getenv(var):
            missing.append(var)
    return missing

@pytest.mark.login
def test_login():
    """
    Positive test: Validate login with correct credentials.
    """
    missing = is_env_configured()
    assert not missing, f"Missing environment variables: {', '.join(missing)}"

    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, data=payload, timeout=10)
        logger.info(f"Login POST to {LOGIN_URL}, status_code={response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during login: {e}")
        pytest.fail(f"Network error: {e}")

    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    # Example: check for login success indicator in response
    try:
        result = response.json()
        assert result.get("success", False), f"Login failed: {result}"
    except Exception as e:
        logger.error(f"Error parsing response JSON: {e}")
        pytest.fail(f"Error parsing response JSON: {e}")

    logger.info("Login test passed.")

if __name__ == "__main__":
    pytest.main([__file__, "--junitxml=login_test_results.xml"])
