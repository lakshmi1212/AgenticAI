# test_login.py
"""
Selenium Python script for: Login Test Case
Validates user login with valid credentials.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuration
LOGIN_URL = "https://example.com/login"
USERNAME = "testuser"
PASSWORD = "securepassword"

class LoginTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run_test(self):
        try:
            self.driver.get(LOGIN_URL)
            time.sleep(2)
            # Enter username
            self.driver.find_element(By.ID, "username").send_keys(USERNAME)
            # Enter password
            self.driver.find_element(By.ID, "password").send_keys(PASSWORD)
            # Submit login form
            self.driver.find_element(By.ID, "loginButton").click()
            time.sleep(3)
            # Validate login success
            assert "Dashboard" in self.driver.title, "Login failed or dashboard not loaded."
            print("Login Test Passed!")
        except Exception as e:
            print(f"Login Test Failed: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    LoginTest().run_test()
