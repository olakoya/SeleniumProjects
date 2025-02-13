'''
3. Pricing Page Class
----------------------

This class represents the pricing page of the dengro.com website.

'''

from base_page1 import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PricingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://dengro.com/pricing/"

    def switch_currency(self, currency_selector, option_selector, price_panel_selector):
        wait = WebDriverWait(self.driver, 10)

        # Click the dropdown to open it
        currency_dropdown = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, currency_selector))
        )
        currency_dropdown.click()

        # Click the specific currency option
        currency_option = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, option_selector))
        )
        currency_option.click()

        # Verify the price panel updates
        price_panel = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, price_panel_selector))
        )
        assert price_panel.is_displayed(), "Currency switch did not update price panel"
        print("✅ Test passed: Currency switch successful")


if __name__ == "__main__":
    from base_page1 import driver  # Ensure base_page1.py correctly initializes and exports the driver

    pricing_page = PricingPage(driver)
    pricing_page.open(pricing_page.url)  # Navigate to the pricing page

    # Replace these with actual CSS selectors from your webpage
    actual_currency_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div.dengro-drop-option.selected"
    actual_option_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div:nth-child(2)"
    actual_price_panel_selector = "#pricing-header > div > div:nth-child(1) > a.dengro-primary-btn"

    pricing_page.switch_currency(actual_currency_selector, actual_option_selector, actual_price_panel_selector)

    driver.quit()  # Close the browser when done






# from base_page1 import BasePage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
# class PricingPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.url = "https://dengro.com/pricing/"
#
#     def switch_currency(self, currency_selector, option_selector, price_panel_selector):
#         wait = WebDriverWait(self.driver, 10)
#
#         # Click the dropdown to open it
#         currency_dropdown = wait.until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, currency_selector))
#         )
#         currency_dropdown.click()
#
#         # Click the specific currency option
#         currency_option = wait.until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, option_selector))
#         )
#         currency_option.click()
#
#         # Verify the price panel updates
#         price_panel = wait.until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, price_panel_selector))
#         )
#         assert price_panel.is_displayed(), "Currency switch did not update price panel"
#         print("✅ Test passed: Currency switch successful")
#
#
# if __name__ == "__main__":
#     from base_page1 import driver  # Ensure base_page1.py correctly initializes and exports the driver
#
#     pricing_page = PricingPage(driver)
#     pricing_page.open(pricing_page.url)  # Navigate to the pricing page
#
#     # Replace these with actual CSS selectors from your webpage
#     actual_currency_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div.dengro-drop-option.selected"
#     actual_option_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div:nth-child(2)"
#     actual_price_panel_selector = "#pricing-header > div > div:nth-child(1) > a.dengro-primary-btn"
#
#     pricing_page.switch_currency(actual_currency_selector, actual_option_selector, actual_price_panel_selector)
#
#     # driver.close()
