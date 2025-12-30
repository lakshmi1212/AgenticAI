# login_test.py
"""
Automated login validation using pytest and requests.
- Credentials and URL are read from environment variables for security.
- Robust error handling and logging included.
- JUnit XML/HTML reporting compatible with pytest plugins.
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
    missing = [var for var in ['LOGIN_URL', 'LOGIN_EMAIL', 'LOGIN_PASSWORD'] if not os.getenv(var)]
    if missing:
        logging.error(f"Missing required environment variables: {', '.join(missing)}")
    return not missing

@pytest.mark.parametrize('email,password,expected', [
    (LOGIN_EMAIL, LOGIN_PASSWORD, True),  # Positive case
    (LOGIN_EMAIL, 'wrongpassword', False),  # Negative case
    ('wrongemail@example.com', LOGIN_PASSWORD, False),  # Negative case
])
def test_login(email, password, expected):
    if not is_env_configured():
        pytest.skip("Environment not configured correctly.")
    assert LOGIN_URL, "LOGIN_URL environment variable not set."

    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        response = session.post(LOGIN_URL, data=payload, timeout=10)
        logging.info(f"POST {LOGIN_URL} -> {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error during login: {e}")
        pytest.fail(f"Network error: {e}")
        return

    if expected:
        assert response.status_code == 200, f"Expected success, got {response.status_code}"
        assert ('dashboard' in response.url or 'success' in response.text.lower()), "Login not successful."
    else:
        assert response.status_code != 200 or ('error' in response.text.lower() or 'invalid' in response.text.lower()), "Expected failure but login succeeded."

# Usage:
#   Set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD environment variables.
#   Run: pytest --maxfail=2 --disable-warnings --junitxml=results.xml Laks/login_test.py
#
# For HTML report: pytest --html=report.html Laks/login_test.py
