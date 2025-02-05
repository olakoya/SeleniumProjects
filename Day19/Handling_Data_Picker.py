from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# Send Keys
# input_date_picker = driver.find_element(By.ID, "datepicker")
# input_date_picker.send_keys("01/06/2025")
'''
Output works as expected
'''
# Send Keys
# input_date_picker = driver.find_element(By.ID, "datepicker")
# input_date_picker.click()

# Year selection (It can be a label or drop down)
# Month selection (It can be a label or drop down)
# Day selection (It can be a label or drop down)

# Date Selection (Most of the time it is a table)

input_date_picker = driver.find_element(By.ID, "datepicker")
input_date_picker.click()

target_year = "2028"
target_month = "April"
target_date = "20"
is_future = True

while True:
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if target_month == current_month and target_year == current_year:
        break
    if is_future:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
