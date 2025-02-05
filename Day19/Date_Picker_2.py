from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date Picker Element
driver.find_element(By.ID, "departon").click()
date_picker_year = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
date_picker_year.select_by_value("2026")
date_picker_month = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
date_picker_month.select_by_value("2026")