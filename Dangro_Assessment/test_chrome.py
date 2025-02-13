import time
from selenium import webdriver
from home_page2 import HomePage
from pricing_page3 import PricingPage
from base_page1 import BasePage
from selenium.webdriver.chrome.options import Options

def setup_browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=options)

def run_tests():
    driver = setup_browser()
    try:
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        pricing_page = PricingPage(driver)

        # Open Home Page
        home_page.open("https://dengro.com/")

        # Accept Cookies
        base_page.click_accept_cookies()

        # Test 1: Verify text presence
        home_page.verify_text_presence("DenGro")

        # Test 2: Click a button
        home_page.click_button("/html/body/div[5]/div/div[1]/div/div/div[1]/a[1]")

        # Test 3: Navigate to pricing page
        home_page.navigate_to_pricing("https://dengro.com/pricing/")

        # Test 4: Switch currency
        pricing_page.open(pricing_page.url)
        pricing_page.switch_currency("select.currency-selector", "div.pricing-panel")

        # Test 5: Capture Screenshot
        home_page.capture_screenshot("chrome_home.png")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()
