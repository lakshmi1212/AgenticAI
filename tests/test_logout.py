# test_logout.py
"""
Selenium script: Logout from the application
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_logout():
    driver = webdriver.Chrome()
    driver.get('https://example.com/login')
    # Login first (reuse login steps for demo)
    driver.find_element(By.ID, 'username').send_keys('valid_user')
    driver.find_element(By.ID, 'password').send_keys('valid_password')
    driver.find_element(By.ID, 'loginBtn').click()
    time.sleep(2)
    # Click logout
    logout_button = driver.find_element(By.ID, 'logoutBtn')
    logout_button.click()
    time.sleep(1)
    # Validate logout success
    assert 'Login' in driver.title, 'Logout failed or Login page not loaded.'
    driver.quit()

if __name__ == '__main__':
    test_logout()
