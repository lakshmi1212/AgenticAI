#!/usr/bin/env python3
"""
Pytest script for automated login validation using Python requests.
Credentials and URL are loaded from environment variables for security.
"""
import os
import pytest
import requests

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.mark.login
def test_login():
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable not set."
    
    payload = {
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }
    try:
        response = requests.post(LOGIN_URL, json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network or connection error: {e}")
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response: {response.text}"
    try:
        resp_json = response.json()
    except Exception:
        pytest.fail("Response is not valid JSON.")
    
    # Customize success criteria below
    assert "token" in resp_json or resp_json.get("success") is True, f"Login failed, response: {resp_json}"
