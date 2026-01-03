import os
import requests
import pytest

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

@pytest.mark.parametrize('email,password', [
    (LOGIN_EMAIL, LOGIN_PASSWORD),
])
def test_login_success(email, password):
    """
    Positive test case: Validates successful login with correct credentials.
    Credentials and URL are sourced from environment variables for security.
    """
    assert LOGIN_URL, 'LOGIN_URL environment variable is not set.'
    assert email, 'LOGIN_EMAIL environment variable is not set.'
    assert password, 'LOGIN_PASSWORD environment variable is not set.'
    try:
        response = requests.post(LOGIN_URL, json={'email': email, 'password': password}, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f'Network error during login request: {e}')
    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}. Response: {response.text}'
    # Further validation can be added for session tokens, user info, etc.
    assert 'token' in response.json() or 'access' in response.json(), 'Login response missing authentication token.'

def test_login_failure():
    """
    Negative test case: Validates failed login with invalid credentials.
    """
    assert LOGIN_URL, 'LOGIN_URL environment variable is not set.'
    try:
        response = requests.post(LOGIN_URL, json={'email': 'invalid@example.com', 'password': 'wrongpassword'}, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f'Network error during login request: {e}')
    assert response.status_code in (400, 401), f'Expected status code 400 or 401, got {response.status_code}. Response: {response.text}'
    assert 'error' in response.json() or 'message' in response.json(), 'Login failure response missing error information.'
