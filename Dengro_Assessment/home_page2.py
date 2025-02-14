'''
2. Home Page Class
--------------------

This class represents the home page of the dengro.com website.

'''

from base_page1 import BasePage  # Import the BasePage class
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://dengro.com"

    def verify_text_presence(self, text):
        try:
            assert text in self.driver.page_source, f"Text '{text}' not found on page {self.url}"
            print(f"Test Passed: '{text}' found on {self.url}")
        except AssertionError as e:
            print(f"Test Failed: {e}")

    def click_button(self, selector, locator_type="css"):
        """Click a button using either CSS selector or XPath."""
        try:
            print(f"DEBUG: Checking existence of element -> {selector} (using {locator_type})")
            by_type = By.XPATH if locator_type == "xpath" else By.CSS_SELECTOR

            # ✅ First, confirm the element **exists** before clicking
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((by_type, selector))
            )
            print(f"DEBUG: Element found -> {selector} (using {locator_type})")

            # ✅ Then, wait for it to be clickable
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((by_type, selector))
            )
            button.click()
            print(f"Test Passed: Clicked button -> {selector} (using {locator_type})")
        except TimeoutException:
            print(f"Test Failed: Element not found or not clickable -> {selector} (using {locator_type})")
        except Exception as e:
            print(f"Test Failed: Unexpected error clicking button -> {selector} (using {locator_type}): {e}")

    def navigate_to_pricing(self, link_xpath):
        """Clicks the Pricing link and ensures the page loads."""
        try:
            print(f"Test Debug: Looking for Pricing link using XPath: {link_xpath}")

            # Wait until the button is clickable
            pricing_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, link_xpath))
            )
            print("Test Debug: Pricing link found, attempting to click...")

            pricing_link.click()
            print("Test Passed: Clicked on Pricing page link")

            # ✅ Wait for a specific element **on the Pricing Page**
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pricing-panel"))
                # <- Change this to an element that exists only on the Pricing page
            )
            print("Test Passed: Pricing page loaded successfully")

            # If the Pricing page opens in a new tab, switch to it
            if len(self.driver.window_handles) > 1:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                print("Test Debug: Switched to new tab")

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Test Failed: Error navigating to Pricing page: {e}")

    def capture_screenshot(self, filename):
        """Captures a screenshot of the current page."""
        try:
            print(f"Camera: Attempting to capture screenshot: {filename}")

            # Verify we are on the right page before capturing screenshot
            print(f"Current URL: {self.driver.current_url}")

            self.driver.save_screenshot(filename)
            print(f"Photo Passed: Screenshot saved: {filename}")
        except Exception as e:
            print(f"Photo Failed: Could not capture screenshot: {e}")
