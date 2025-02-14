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
        home_page.click_button("/html/body/div[5]/div/div[1]/div/div/div[1]/a[1]", locator_type="xpath")

        # Test 3: Navigate to pricing page (Added delay)
        time.sleep(3)  # Ensure page is fully loaded before finding the Pricing link
        home_page.navigate_to_pricing("/html/body/div[5]/header/div/div/div/div[1]/nav/div/div/div/div/ul/li[2]/a/span")

        # Test 4: Switch currency (Using correct selectors)
        pricing_page.open(pricing_page.url)
        pricing_page.switch_currency(
            "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div.dengro-drop-option.selected",
            "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div:nth-child(2)",
            "#pricing-header > div > div:nth-child(1) > a.dengro-primary-btn"
        )

        # Test 5: Capture Screenshot
        try:
            print("Test Debug: Waiting before capturing screenshot...")
            time.sleep(5)  # Wait a few seconds to ensure page is fully loaded
            home_page.capture_screenshot("chrome_home.png")
            print("Test Passed: Screenshot captured successfully")
        except Exception as e:
            print(f"Test Failed: Could not capture screenshot: {e}")

    finally:
        # Ensure the browser is closed after tests
        driver.quit()

if __name__ == "__main__":
    run_tests()

    # Remove input() for automation runs
    # input("Press Enter to exit and close the browser...")
