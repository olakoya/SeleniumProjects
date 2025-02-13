'''
4. Test Suite
---------------

This class contains the test cases and runs them for multiple browsers using "Chrome" and "Edge".

'''

import time
from selenium import webdriver
from home_page2 import HomePage
from pricing_page3 import PricingPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Ensure webdriver_manager is installed
from selenium.webdriver.edge.service import Service as EdgeService


def setup_browser(browser_name):
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return webdriver.Chrome(options=options)

    elif browser_name == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--inprivate")  # Edge equivalent of incognito
        edge_service = EdgeService(EdgeChromiumDriverManager().install())  # Ensure correct Edge WebDriver
        return webdriver.Edge(service=edge_service, options=edge_options)

    else:
        raise ValueError("Unsupported browser!")


def run_tests():
    browsers = ["chrome", "edge"]  # Running on Chrome and Edge
    for browser in browsers:
        driver = setup_browser(browser)
        try:
            # Initialize pages
            home_page = HomePage(driver)
            pricing_page = PricingPage(driver)

            # Test 1: Verify text presence on the home page
            home_page.open("https://dengro.com/")
            home_page.verify_text_presence("DenGro")

            # Test 2: Click a button on the home page
            home_page.click_button("#hero-item-3 > div.col.content > a.hero-btn.dengro-primary-btn")

            # Test 3: Navigate to the pricing page
            home_page.navigate_to_pricing("#modal-1-content > ul > li:nth-child(2) > a > span")

            # Test 4: Switch currency on the pricing page
            pricing_page.open("https://dengro.com/pricing/")
            pricing_page.switch_currency("select.currency-selector", "div.pricing-panel")

            # Test 5: Capture a screenshot of the home page
            home_page.open("https://dengro.com/")
            home_page.capture_screenshot(f"{browser}_home.png")

        finally:
            if driver:
                driver.quit()


if __name__ == "__main__":
    run_tests()
