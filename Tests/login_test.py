# login_test.py
"""
Automated login validation test using pytest and requests.
- Credentials and login URL are securely parameterized via environment variables.
- Robust error handling and logging for network/authentication issues.
- Designed for integration with DevOps/CI pipelines.
"""
import os
import logging
import pytest
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@pytest.mark.parametrize("case, email, password, expected", [
    ("valid", os.getenv('LOGIN_EMAIL'), os.getenv('LOGIN_PASSWORD'), True),
    ("invalid_password", os.getenv('LOGIN_EMAIL'), "invalid_pass", False),
    ("invalid_email", "invalid@example.com", os.getenv('LOGIN_PASSWORD'), False),
])
def test_login(case, email, password, expected):
    """
    Test login endpoint with different credential scenarios.
    Requires environment variables:
      - LOGIN_URL
      - LOGIN_EMAIL
      - LOGIN_PASSWORD
    """
    url = os.getenv('LOGIN_URL')
    assert url and email and password, f"Missing credentials or URL for case: {case}"
    session = requests.Session()
    payload = {'email': email, 'password': password}
    try:
        response = session.post(url, data=payload, timeout=10)
        logging.info(f"[{case}] POST {url} -> {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"[{case}] Network error: {e}")
        assert not expected, f"[{case}] Network error in positive test: {e}"
        return
    if expected:
        assert response.status_code == 200, f"[{case}] Login failed: {response.text}"
        assert ("dashboard" in response.url or "success" in response.text.lower()), f"[{case}] Login not successful: {response.text}"
    else:
        assert response.status_code != 200 or "error" in response.text.lower(), f"[{case}] Negative test should fail, but succeeded."
