'''
4. Table with div Tags
-----------------------
These are tables without no tag names or table names

E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://htmltable.com/div-table/")
driver.maximize_window()

rows = driver.find_elements(By.XPATH, "//div[contains(@class,'divTable blueDemoTable')]//div[@class='divTableBody']//div[@class='divTableRow']")
print(len(rows))

for row in rows:
    print(row.text)

'''
Output is
3
'''

driver.quit()