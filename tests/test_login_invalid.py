# test_login_invalid.py
"""
Test Case: Login with invalid credentials
Steps:
1. Open the login page
2. Enter invalid username
3. Enter invalid password
4. Click login
5. Verify error message
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestLoginInvalid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_invalid(self):
        driver = self.driver
        driver.get('https://example.com/login')
        driver.find_element(By.ID, 'username').send_keys('invalid_user')
        driver.find_element(By.ID, 'password').send_keys('invalid_password')
        driver.find_element(By.ID, 'loginBtn').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'errorMsg').text
        self.assertIn('Invalid credentials', error_message)
        # Add more assertions as needed

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
