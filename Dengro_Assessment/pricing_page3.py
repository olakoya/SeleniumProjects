'''
3. Pricing Page Class
----------------------

This class represents the pricing page of the dengro.com website.

'''

from base_page1 import BasePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys

# Get browser choice from command line arguments
browser = sys.argv[1] if len(sys.argv) > 1 else "chrome"

if browser == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
elif browser == "edge":
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=edge_options)
else:
    raise ValueError("Unsupported browser!")

class PricingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://dengro.com/pricing/"

    def switch_currency(self, currency_selector, option_selector, price_panel_selector):
        """Switch currency and verify price panel update."""
        wait = WebDriverWait(self.driver, 10)

        # Click the dropdown to open it
        currency_dropdown = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, currency_selector))
        )
        currency_dropdown.click()
        print("Test Passed: Clicked currency dropdown")

        # Click the specific currency option
        currency_option = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, option_selector))  # Passed FIXED
        )
        currency_option.click()
        print("Test Passed: Selected currency option")

        # Verify the price panel updates
        price_panel = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, price_panel_selector))
        )
        assert price_panel.is_displayed(), "Test Failed: Currency switch did not update price panel"
        print("Test Passed: Currency switch successful")

if __name__ == "__main__":
    pricing_page = PricingPage(driver)
    pricing_page.open(pricing_page.url)  # Navigate to the pricing page

    # Replace these with actual CSS selectors from your webpage
    actual_currency_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div.dengro-drop-option.selected"
    actual_option_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div:nth-child(2)"
    actual_price_panel_selector = "#pricing-header > div > div:nth-child(1) > a.dengro-primary-btn"

    pricing_page.switch_currency(actual_currency_selector, actual_option_selector, actual_price_panel_selector)

    # Keep browser open for debugging
    driver.implicitly_wait(10)
    # input("Press Enter to exit and close the browser...")  # Commented out for automation

    # driver.close()  # Use driver.quit() instead to close all tabs
    driver.quit()
