'''
1. Base Page Class
--------------------

This class contains common methods and utilities that can be reused across all pages.

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):  # __init__ method takes a driver and assigns it to an instance variable
        self.driver = driver

    def open(self, url):  # Navigate to a specific URL
        print(f"Opening URL: {url}")
        self.driver.get(url)
        print(f"Page loaded: {self.driver.title}")

    def find_element(self, by, value):  # Wrap Selenium’s native method for locating elements
        return self.driver.find_element(by, value)

    def wait_for_element(self, by, value, timeout=10):
        """Waits for an element to be present on the page."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click_accept_cookies(self):
        """Clicks the accept cookies button if it appears."""
        try:
            print("Checking for cookie banner...")
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                    "body > div.cky-consent-container.cky-box-bottom-left > div > div > div > "
                    "div.cky-notice-btn-wrapper > button.cky-btn.cky-btn-accept"))
            )
            print("Cookie banner found, attempting to click...")
            cookie_button.click()
            print("Cookies accepted successfully!")
        except Exception as e:
            print("No cookie banner found or already accepted:", e)

    def capture_screenshot(self, filename):
        """Captures a screenshot of the current page."""
        try:
            self.driver.save_screenshot(filename)
            print(f"Screenshot saved as {filename}")
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
