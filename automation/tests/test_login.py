# test_login.py
"""
Selenium Python script for automated login test.
Validated Test Case:
- Title: Login Functionality
- Steps:
    1. Launch browser and navigate to login page.
    2. Enter valid username and password.
    3. Click login button.
    4. Verify successful login (e.g., dashboard is visible).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'loginBtn')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        try:
            # Example: check for dashboard element
            dashboard = self.driver.find_element(By.ID, 'dashboard')
            return dashboard.is_displayed()
        except NoSuchElementException:
            return False


def test_login():
    driver = webdriver.Chrome()
    driver.get('https://example.com/login')
    login_page = LoginPage(driver)
    login_page.login('valid_user', 'valid_password')
    time.sleep(2)  # Wait for page to load
    assert login_page.is_logged_in(), 'Login failed: dashboard not visible.'
    driver.quit()

if __name__ == '__main__':
    test_login()
