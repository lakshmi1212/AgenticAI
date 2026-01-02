#!/usr/bin/env python
"""
Test Case: User Logout Functionality
Validates that a logged-in user can log out and is redirected to the login page.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogout:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # Precondition: User is logged in
        self.driver.get('https://your-app-url.com/login')
        self.driver.find_element(By.ID, 'username').send_keys('valid_user')
        self.driver.find_element(By.ID, 'password').send_keys('valid_password')
        self.driver.find_element(By.ID, 'loginBtn').click()
        assert 'Dashboard' in self.driver.title or self.driver.find_element(By.ID, 'dashboard').is_displayed()

    def teardown_method(self):
        self.driver.quit()

    def test_logout(self):
        driver = self.driver
        # Click logout button
        logout_button = driver.find_element(By.ID, 'logoutBtn')
        logout_button.click()
        # Verify redirect to login page
        assert 'Login' in driver.title or driver.find_element(By.ID, 'login').is_displayed()

if __name__ == '__main__':
    pytest.main([__file__])
