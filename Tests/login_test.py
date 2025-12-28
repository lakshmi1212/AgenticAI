# login_test.py
"""
Automated pytest script for login validation.
Credentials and URL are sourced from environment variables for security.
Generates JUnit XML test reports for CI/CD integration.
"""
import os
import logging
import pytest
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

@pytest.mark.login
@pytest.mark.parametrize("case, email, password, expected_status", [
    ("valid", os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"), 200),
    ("invalid_password", os.getenv("LOGIN_EMAIL"), "invalid_pass", 401),
    ("invalid_email", "invalid@email.com", os.getenv("LOGIN_PASSWORD"), 401)
])
def test_login(case, email, password, expected_status):
    """
    Login test with positive and negative cases.
    Environment variables required: LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
    """
    url = os.getenv('LOGIN_URL')
    assert url, 'LOGIN_URL not set as environment variable.'
    assert email, 'Email not provided.'
    assert password, 'Password not provided.'
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        response = session.post(url, data=payload, timeout=10)
        logger.info(f"Test case: {case}, Status: {response.status_code}, Response: {response.text[:100]}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during login: {e}")
        pytest.fail(f"Network error: {e}")
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}: {response.text}"
    if case == "valid":
        assert ('dashboard' in response.url or 'success' in response.text.lower()), "Login not successful."

# To run:
#   export LOGIN_URL=https://example.com/login
#   export LOGIN_EMAIL=user@example.com
#   export LOGIN_PASSWORD=securepassword
#   pytest --junitxml=report.xml Tests/login_test.py
