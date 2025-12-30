# login_test.py
"""
Automated login test using pytest and requests.
Credentials and login URL are securely loaded from environment variables.
Includes robust error handling and logging for DevOps integration.
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

def is_env_configured():
    return all([LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD])

@pytest.mark.parametrize("email,password,expected", [
    (LOGIN_EMAIL, LOGIN_PASSWORD, True), # Positive test
    (LOGIN_EMAIL, "wrong_password", False), # Negative test
    ("wrong_email@example.com", LOGIN_PASSWORD, False), # Negative test
])
def test_login(email, password, expected):
    if not is_env_configured():
        pytest.skip("Environment variables LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD must be set.")
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        logging.info(f"Attempting login for email: {email}")
        response = session.post(LOGIN_URL, data=payload, timeout=10)
    except requests.RequestException as e:
        logging.error(f"Network error during login: {e}")
        assert not expected, f"Expected failure due to network error, got exception: {e}"
        return
    logging.info(f"Login response status: {response.status_code}")
    if expected:
        assert response.status_code == 200, f"Login failed: {response.text}"
        assert ("dashboard" in response.url or "success" in response.text.lower()), "Login not successful."
    else:
        assert response.status_code != 200 or "error" in response.text.lower(), "Negative login should fail."
