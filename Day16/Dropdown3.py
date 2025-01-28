'''


The reusable code below is called BOILER PLAY CODES
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("selenium")

