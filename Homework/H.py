from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
import time

def setup_browser(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome()
    elif browser_name == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser!")

def test_text_presence(driver, url, text):
    driver.get(url)
    assert text in driver.page_source, f"Text '{text}' not found on page {url}"
    print(f"Test passed: '{text}' found on {url}")

def test_button_click(driver, url, button_selector):
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, button_selector)
    button.click()
    print("Button clicked successfully")
    time.sleep(2)

def test_link_navigation(driver, url, link_selector, expected_url):
    driver.get(url)
    link = driver.find_element(By.CSS_SELECTOR, link_selector)
    link.click()
    time.sleep(2)
    assert driver.current_url == expected_url, f"Navigation failed: Expected {expected_url}, got {driver.current_url}"
    print(f"Test passed: Navigation to {expected_url} successful")

def test_currency_switch(driver, url, currency_selector, price_panel_selector):
    driver.get(url)
    currency_dropdown = driver.find_element(By.CSS_SELECTOR, currency_selector)
    currency_dropdown.click()
    currency_dropdown.send_keys(Keys.DOWN, Keys.ENTER)
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, price_panel_selector).is_displayed(), "Currency switch did not update price panel"
    print("Test passed: Currency switch successful")

def capture_screenshot(driver, url, filename):
    driver.get(url)
    driver.save_screenshot(filename)
    print(f"Screenshot saved as {filename}")

def run_tests():
    browsers = ["chrome", "firefox"]
    for browser in browsers:
        driver = setup_browser(browser)
        try:
            test_text_presence(driver, "https://dengro.com", "DenGro")
            test_button_click(driver, "https://dengro.com", "button.cta")
            test_link_navigation(driver, "https://dengro.com", "a[href='/pricing']", "https://dengro.com/pricing")
            test_currency_switch(driver, "https://dengro.com/pricing", "select.currency-selector", "div.pricing-panel")
            capture_screenshot(driver, "https://dengro.com", "dengro_home.png")
        finally:
            driver.quit()

if __name__ == "__main__":
    run_tests()
