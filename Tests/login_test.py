import os
import pytest
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.parametrize("email,password,expected_status", [
    (LOGIN_EMAIL, LOGIN_PASSWORD, 200),  # Positive test case
])
def test_login(email, password, expected_status):
    """
    Test login endpoint with provided credentials.
    Credentials are securely loaded from environment variables.
    """
    if not LOGIN_URL or not email or not password:
        pytest.skip("Required environment variables not set: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD")

    try:
        response = requests.post(
            LOGIN_URL,
            json={"email": email, "password": password},
            timeout=10
        )
        logging.info(f"Request to {LOGIN_URL} returned status {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Network error during login request: {e}")
        pytest.fail(f"Network error during login request: {e}")

    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}. Response: {response.text}"
    # Optionally, validate response content for successful login
    # assert 'token' in response.json(), "No token returned in successful login response"