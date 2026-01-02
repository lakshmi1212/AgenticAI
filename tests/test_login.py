"""
test_login.py
Automated Selenium test for login functionality.
Validated Test Case:
- Title: Login with valid credentials
- Steps:
    1. Navigate to the login page
    2. Enter valid username and password
    3. Click the login button
    4. Verify successful login (dashboard is displayed)
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://example.com/login")  # Update with real login URL
        # Enter username
        username = driver.find_element(By.ID, "username")
        username.clear()
        username.send_keys("valid_user")
        # Enter password
        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("valid_password")
        # Click login
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(2)
        # Verify dashboard appears
        try:
            dashboard = driver.find_element(By.ID, "dashboard")
            self.assertTrue(dashboard.is_displayed(), "Dashboard is not displayed after login.")
        except NoSuchElementException:
            self.fail("Dashboard element not found - login may have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
