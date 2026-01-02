# test_login_valid.py
"""
Test Case: Login with valid credentials
Steps:
1. Open the login page
2. Enter valid username
3. Enter valid password
4. Click login
5. Verify successful login
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestLoginValid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://example.com/login')
        driver.find_element(By.ID, 'username').send_keys('valid_user')
        driver.find_element(By.ID, 'password').send_keys('valid_password')
        driver.find_element(By.ID, 'loginBtn').click()
        time.sleep(2)
        self.assertIn('dashboard', driver.current_url)
        # Add more assertions as needed

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
