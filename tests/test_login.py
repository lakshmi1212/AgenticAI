"""
Selenium Test Script: Login Functionality
Generated automatically from validated test case
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.base_url = "https://example.com/login"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_valid_login(self):
        driver = self.driver
        driver.get(self.base_url)
        # Enter username
        driver.find_element(By.ID, "username").send_keys("testuser")
        # Enter password
        driver.find_element(By.ID, "password").send_keys("securepassword")
        # Submit form
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(2)
        # Assert login success
        try:
            welcome = driver.find_element(By.ID, "welcomeMessage")
            self.assertIn("Welcome", welcome.text)
        except NoSuchElementException:
            self.fail("Login failed: Welcome message not found.")

    def test_invalid_login(self):
        driver = self.driver
        driver.get(self.base_url)
        # Enter invalid credentials
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(2)
        # Assert error message
        try:
            error = driver.find_element(By.ID, "errorMessage")
            self.assertIn("Invalid", error.text)
        except NoSuchElementException:
            self.fail("Error message not found for invalid login.")

if __name__ == "__main__":
    unittest.main()
