from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.booking.com/flights/")  # Replace with actual flight booking URL

# Click on the date picker to open the calendar
input_date_picker = driver.find_element(By.XPATH, "//span[@class='Text-module__root--variant-body_2___7cHHf']")  # Replace with the actual ID
input_date_picker.click()

# Wait for the calendar to appear
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "Calendar-module__cell___fB9kz"))  # Replace with actual class
)

# Select Departure Date (8 March)
departure_date = driver.find_element(By.XPATH, "//td[@data-date='8'][@data-month='2']")  # Adjust for website
departure_date.click()

# Select Return Date (15 March)
return_date = driver.find_element(By.XPATH, "//td[@data-date='15'][@data-month='2']")
return_date.click()

print("Successfully selected flight dates!")

driver.quit()
