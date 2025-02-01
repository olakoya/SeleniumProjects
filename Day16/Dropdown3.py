'''
Dropdown
---------
- This is the auto suggest dropdown
- Dropdown with hidden items

- Explicit wait = Declaration + Usage
- Declaration ==> WebDriver Class

- ctrl+/ or frwdslash/

- Freezing th4 screen is required


The reusable code below is called BOILER PLAY CODES
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()

mywait = WebDriverWait(driver, 10) # Declaration

driver.find_element(By.NAME, "q").send_keys("selenium")
# time.sleep(3)
options = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li")
# options = mywait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@@role='listbox']//li")))
print(len(options))

for option in options:
    # print(option.text)
    if option.text == "selenium download":
        option.click()
        break

'''
Output is 
Title: Test Passed

Output after adding lines 31 and 36
True
'''


driver.quit()

