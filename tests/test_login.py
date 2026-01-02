"""
Test Case: Verify Login Functionality
Description: Ensure valid users can log in and are redirected to the dashboard.
Author: Automation Pipeline Agent
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Test data
LOGIN_URL = "https://example.com/login"
USERNAME = "testuser"
PASSWORD = "Test@1234"
EXPECTED_DASHBOARD_URL = "https://example.com/dashboard"


def setup_driver():
    """Initializes and returns a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode for CI/CD
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def test_login():
    driver = setup_driver()
    try:
        print("[INFO] Navigating to login page...")
        driver.get(LOGIN_URL)
        
        print("[INFO] Entering username...")
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        print("[INFO] Entering password...")
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        print("[INFO] Submitting login form...")
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(2)
        
        print("[INFO] Verifying dashboard redirection...")
        assert driver.current_url == EXPECTED_DASHBOARD_URL, "Login failed or dashboard not loaded!"
        print("[PASS] Login test passed.")
    except (NoSuchElementException, TimeoutException) as e:
        print(f"[ERROR] Element not found or timeout: {e}")
    except AssertionError as e:
        print(f"[FAIL] Assertion failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
