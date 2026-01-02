# test_logout.py
"""
Selenium Python script for: Logout Test Case
Validates user logout functionality.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuration
DASHBOARD_URL = "https://example.com/dashboard"
USERNAME = "testuser"
PASSWORD = "securepassword"

class LogoutTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(DASHBOARD_URL)
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys(USERNAME)
        self.driver.find_element(By.ID, "password").send_keys(PASSWORD)
        self.driver.find_element(By.ID, "loginButton").click()
        time.sleep(3)

    def run_test(self):
        try:
            self.login()
            # Click logout
            self.driver.find_element(By.ID, "logoutButton").click()
            time.sleep(2)
            # Validate logout success
            assert "Login" in self.driver.title, "Logout failed or login page not loaded."
            print("Logout Test Passed!")
        except Exception as e:
            print(f"Logout Test Failed: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    LogoutTest().run_test()
