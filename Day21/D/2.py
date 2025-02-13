from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from _pytest.config import get_plugin_manager
import time

# Function to initialize the browser driver
def initialize_browser(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver

# Function to test functionality
def test_dengro_functionality(browser_name):
    driver = initialize_browser(browser_name)
    driver.get("https://dengro.com")

    try:
        # 1. Assert that a piece of text appears on a given page
        assert "Practice growth never felt so easy" in driver.page_source, "Text not found on page"

        # 2. Assert clicking a button does some functionality
        button = driver.find_element(By.CSS_SELECTOR, "button.cta-button")
        button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("new-page"))
        assert "new-page" in driver.current_url, "Button click did not navigate correctly"

        # 3. Assert clicking a link navigates correctly
        link = driver.find_element(By.LINK_TEXT, "Pricing")
        link.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://dengro.com/pricing"))
        assert driver.current_url == "https://dengro.com/pricing", "Link navigation failed"

        # 4. Assert that the pricing page allows users to change their currency
        currency_dropdown = driver.find_element(By.ID, "currency-dropdown")
        currency_dropdown.click()
        currency_dropdown.find_element(By.XPATH, "//option[text()='EUR']").click()
        time.sleep(2)  # Wait for the page to update

        price_element = driver.find_element(By.CLASS_NAME, "price-panel")
        assert "€" in price_element.text, "Currency change did not reflect in pricing"

        # 5. Capture a screenshot of any page
        driver.save_screenshot(f"{browser_name}_screenshot.png")

    finally:
        driver.quit()

# Run tests for Chrome and Edge
test_dengro_functionality("chrome")
test_dengro_functionality("edge")