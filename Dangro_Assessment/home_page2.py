'''
2. Home Page Class
--------------------

This class represents the home page of the dengro.com website.

'''

from base_page1 import BasePage # Import the BasePage class
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://dengro.com"

    def verify_text_presence(self, text):
        assert text in self.driver.page_source, f"Text '{text}' not found on page {self.url}"
        print(f"Test passed: '{text}' found on {self.url}")

    def click_button(self, button_selector):
        button = self.find_element(By.CSS_SELECTOR, button_selector)
        button.click()
        print("Button clicked successfully")

    def navigate_to_pricing(self, link_selector):
        pricing_link = self.find_element(By.CSS_SELECTOR, link_selector)
        pricing_link.click()
        print("Navigated to Pricing page")