"""
Test Case: Verify Login Functionality
Steps:
1. Open login page
2. Enter valid username and password
3. Click login
4. Verify successful login (e.g., dashboard displayed)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
import time

# Configurable parameters
LOGIN_URL = "https://example.com/login"
USERNAME = "testuser"
PASSWORD = "securepassword"

# Page Object Model for Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def enter_username(self, username):
        user_field = self.driver.find_element(By.ID, "username")
        user_field.clear()
        user_field.send_keys(username)
    def enter_password(self, password):
        pass_field = self.driver.find_element(By.ID, "password")
        pass_field.clear()
        pass_field.send_keys(password)
    def click_login(self):
        self.driver.find_element(By.ID, "loginBtn").click()

# Utility function for login test
def test_login():
    # Setup Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService())
    driver.maximize_window()
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()
    time.sleep(2)  # Wait for login to process
    # Verification
    try:
        dashboard = driver.find_element(By.ID, "dashboard")
        assert dashboard.is_displayed(), "Dashboard not displayed after login."
        print("Login test passed.")
    except NoSuchElementException:
        print("Login test failed: Dashboard not found.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
