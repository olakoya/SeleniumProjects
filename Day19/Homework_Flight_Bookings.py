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
driver.get("https://www.booking.com/flights/")
driver.maximize_window()

input_date_picker = driver.find_element(By.XPATH, "//span[@class='Text-module__root--variant-body_2___7cHHf']")
input_date_picker.send_keys("Sat 8 Mar - Sat 15 Mar")

driver.close()