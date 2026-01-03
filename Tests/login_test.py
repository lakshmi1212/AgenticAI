import os
import requests
import pytest

LOGIN_URL = os.environ.get("LOGIN_URL")
LOGIN_EMAIL = os.environ.get("LOGIN_EMAIL")
LOGIN_PASSWORD = os.environ.get("LOGIN_PASSWORD")

@pytest.mark.parametrize("email,password", [(LOGIN_EMAIL, LOGIN_PASSWORD)])
def test_login(email, password):
    assert LOGIN_URL, "LOGIN_URL must be set as environment variable."
    assert email, "LOGIN_EMAIL must be set as environment variable."
    assert password, "LOGIN_PASSWORD must be set as environment variable."
    session = requests.Session()
    try:
        response = session.post(
            LOGIN_URL,
            data={"email": email, "password": password},
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    # Check for successful login
    try:
        json_data = response.json()
        if "token" in json_data:
            assert json_data["token"], "Login token not found in response."
    except Exception:
        if response.history:
            assert response.history[0].status_code == 302, "Expected redirect after login."
        else:
            assert "login successful" in response.text.lower() or "dashboard" in response.text.lower(), "Login failed or response not recognized."
