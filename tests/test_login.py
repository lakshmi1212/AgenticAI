#!/usr/bin/env python3
"""
Selenium automation script for validated test case: Login functionality
Author: Automation Agent
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestLogin(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def test_login_valid_user(self):
        driver = self.driver
        driver.get('https://example.com/login')
        driver.find_element(By.ID, 'username').send_keys('valid_user')
        driver.find_element(By.ID, 'password').send_keys('valid_password')
        driver.find_element(By.ID, 'loginBtn').click()
        self.assertIn('Dashboard', driver.title)

    def test_login_invalid_user(self):
        driver = self.driver
        driver.get('https://example.com/login')
        driver.find_element(By.ID, 'username').send_keys('invalid_user')
        driver.find_element(By.ID, 'password').send_keys('wrong_password')
        driver.find_element(By.ID, 'loginBtn').click()
        error = driver.find_element(By.ID, 'errorMsg').text
        self.assertEqual(error, 'Invalid credentials')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
