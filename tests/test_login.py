# test_login.py
"""
Selenium script: Login with valid credentials
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():
    # Setup WebDriver (Chrome)
    driver = webdriver.Chrome()
    driver.get('https://example.com/login')
    
    # Enter username
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('valid_user')
    
    # Enter password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('valid_password')
    
    # Submit form
    login_button = driver.find_element(By.ID, 'loginBtn')
    login_button.click()
    
    time.sleep(2)  # Wait for login to process
    
    # Validate login success
    assert 'Dashboard' in driver.title, 'Login failed or Dashboard not loaded.'
    
    driver.quit()

if __name__ == '__main__':
    test_login()
