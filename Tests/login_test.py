import os
import requests
import pytest
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

@pytest.mark.parametrize("login_url, email, password", [
    (LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD)
])
def test_login_positive(login_url, email, password):
    """
    Positive test: Validates successful login with correct credentials.
    Expects 200 or 302 response and presence of authentication token/session.
    """
    assert login_url, "LOGIN_URL not set in environment variables"
    assert email, "LOGIN_EMAIL not set in environment variables"
    assert password, "LOGIN_PASSWORD not set in environment variables"

    payload = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(login_url, data=payload, timeout=10)
        logging.info(f"Login response status: {response.status_code}")
        assert response.status_code in (200, 302), f"Unexpected status: {response.status_code}"
        # Check for session/auth cookie or token
        assert ('Set-Cookie' in response.headers or 'token' in response.text or 'session' in response.text), "No authentication indicator found in response."
    except requests.RequestException as e:
        logging.error(f"Network or request error: {e}")
        pytest.fail(f"Login request failed: {e}")
    except AssertionError as ae:
        logging.error(f"Assertion failed: {ae}")
        pytest.fail(str(ae))

# Edge case: Invalid password
@pytest.mark.parametrize("login_url, email, password", [
    (LOGIN_URL, LOGIN_EMAIL, "invalid_password")
])
def test_login_negative(login_url, email, password):
    """
    Negative test: Validates login fails with incorrect password.
    Expects 401, 403, or error message.
    """
    assert login_url, "LOGIN_URL not set in environment variables"
    assert email, "LOGIN_EMAIL not set in environment variables"

    payload = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(login_url, data=payload, timeout=10)
        logging.info(f"Negative login response status: {response.status_code}")
        assert response.status_code in (401, 403, 400), f"Expected failure status, got {response.status_code}"
    except requests.RequestException as e:
        logging.error(f"Network or request error: {e}")
        pytest.fail(f"Login request failed: {e}")
    except AssertionError as ae:
        logging.error(f"Assertion failed: {ae}")
        pytest.fail(str(ae))
