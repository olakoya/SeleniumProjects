from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach", True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switch to iframe (if the date picker is inside an iframe)
driver.switch_to.frame(0)

# Click on date input field to open calendar
input_date_picker = driver.find_element(By.ID, "datepicker")
input_date_picker.click()

# Target date selection
target_year = "2028"
target_month = "April"
target_date = "20"

# Automatically determine if we need to go forward or backward
current_year = int(driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text)
target_year = int(target_year)
is_future = target_year > current_year

# Loop until the correct month and year are found
while True:
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if target_month == current_month and str(target_year) == current_year:
        break

    if is_future:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

# Select the target date
driver.find_element(By.XPATH, f"//a[text()='{target_date}']").click()

print(f"Successfully selected: {target_date}-{target_month}-{target_year}")

# driver.quit()
