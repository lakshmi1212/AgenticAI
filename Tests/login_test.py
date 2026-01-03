import os
import requests
import pytest

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.parametrize("email,password,expected_status", [
    (LOGIN_EMAIL, LOGIN_PASSWORD, 200),  # Positive test case
])
def test_login(email, password, expected_status):
    """
    Test login functionality by sending credentials to the login endpoint.
    Credentials are loaded from environment variables for security.
    """
    if not LOGIN_URL or not email or not password:
        pytest.skip("Missing LOGIN_URL or credentials in environment variables.")
    try:
        response = requests.post(
            LOGIN_URL,
            json={"email": email, "password": password},
            timeout=10
        )
    except requests.RequestException as e:
        pytest.fail(f"Network or connection error during login: {e}")
    assert response.status_code == expected_status, (
        f"Login failed. Expected status {expected_status}, got {response.status_code}. Response: {response.text}"
    )
    # Optionally validate response structure for successful login
    if response.status_code == 200:
        assert "token" in response.json() or "session" in response.json(), "No authentication token/session returned."
