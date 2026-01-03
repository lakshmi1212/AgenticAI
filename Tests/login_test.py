#!/usr/bin/env python3
"""
Pytest login automation for validating authentication endpoint using environment variables for credentials.

- LOGIN_URL: Endpoint for login
- LOGIN_EMAIL: Email for login
- LOGIN_PASSWORD: Password for login

This script performs a positive login test and reports results. Credentials are read from environment variables for security.
"""
import os
import pytest
import requests

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login_positive():
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable not set."
    try:
        resp = requests.post(
            LOGIN_URL,
            json={"email": LOGIN_EMAIL, "password": LOGIN_PASSWORD},
            timeout=10
        )
    except requests.RequestException as e:
        pytest.fail(f"Network error during login request: {e}")
    assert resp.status_code == 200, f"Unexpected status code: {resp.status_code}, Response: {resp.text}"
    # You may need to adapt the following assertion depending on your API response
    assert "token" in resp.json() or resp.json().get("success", False), "Login did not succeed: {resp.text}"
