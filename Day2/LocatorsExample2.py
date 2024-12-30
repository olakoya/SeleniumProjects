from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()

# Create the Service object
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with Service and options
driver = webdriver.Chrome(service=service, options=options)

try:
    # Perform your tasks
    print("Navigated to the website")
    driver.get("http://www.automationpractice.pl/index.php")
    driver.maximize_window()

    # Wait for the search box
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "search_query_top"))
    )
    print("Typing in the search box")
    search_box.send_keys("T-shirts")

    # Wait for the search button
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "submit_search"))
    )
    print("Clicking the search button")
    search_button.click()

    # Wait for item to display
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Printed Chiffon Dress"))
    )
    print("Search item selected")
    search_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    print("Closing the browser")
    driver.quit()

'''
Output is
Navigated to the website
Typing in the search box
Clicking the search button
Search item selected
Closing the browser
'''