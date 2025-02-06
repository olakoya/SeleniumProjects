from selenium import webdriver
from selenium.webdriver.common.by import By

def select_date(driver, target_year, target_month, target_date, is_future ):

    while True:
        current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        if target_month == current_month and target_year == current_year:
            break
        if is_future:
            driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        else:
            driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

    dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    for date in dates:
        if date.text == target_date:
            date.click()
            break

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


# Day selection (It can be a label or drop down)

# Date Selection (Most of the time it is a table)

input_date_picker = driver.find_element(By.ID, "datepicker")
input_date_picker.click()

target_year = "2028"
target_month = "April"
target_date = "20"
is_future = True

# target_year = "2018"
# target_month = "April"
# target_date = "12"
# is_future = False

# Calling function in lines 4 to 20
select_date(driver, target_year, target_month, target_date, is_future)

driver.quit()

