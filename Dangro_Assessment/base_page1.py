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
    def __init__(self, driver): # __init__ method takes a driver and assigns it to an instance variable
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click_accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.cky-consent-container.cky-box-bottom-left > div > div > div > "
                                                             "div.cky-notice-btn-wrapper > button.cky-btn.cky-btn-accept"))
            )
            cookie_button.click()
            print("Cookies accepted successfully!")
        except Exception as e:
            print("No cookie banner found or already accepted:", e)

    def open(self, url): # This method allows to navigate to a specific URL
        self.driver.get(url)

    def find_element(self, by, value): # This method wrap Selenium’s native methods for element location
        return self.driver.find_element(by, value)

    def wait_for_element(self, by, value, timeout=10): # This method uses Selenium’s WebDriverWait along with expected_conditions to wait until an element is present
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def capture_screenshot(self, filename): # This method saves a screenshot of the current page and prints a confirmation message.
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved as {filename}")