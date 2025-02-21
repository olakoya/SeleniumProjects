'''

right click() --> context_click()

'''

# Boiler Codes are reused to begin the code lines i.e. importing libraries from selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=en-uk")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

act = ActionChains(driver) # act is object reference variable

# Right Click Mouse Operations
ele = driver.find_element(By.XPATH, "//span[text()='right click me']")
act.context_click(ele).perform()
act.scroll_to_element()