#!/usr/bin/env python3
"""
Automated login validation using pytest and requests.
Credentials and login URL are managed via environment variables for security.
"""
import os
import requests
import pytest

LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

@pytest.mark.parametrize("email,password", [(LOGIN_EMAIL, LOGIN_PASSWORD)])
def test_login(email, password):
    assert LOGIN_URL, "LOGIN_URL environment variable is not set."
    assert email, "LOGIN_EMAIL environment variable is not set."
    assert password, "LOGIN_PASSWORD environment variable is not set."
    payload = {"email": email, "password": password}
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.RequestException as e:
        pytest.fail(f"Network or connection error: {e}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    try:
        data = response.json()
    except Exception:
        pytest.fail("Response is not valid JSON.")
    assert "token" in data or data.get("success", False), f"Login failed or unexpected response: {data}"
