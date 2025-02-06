'''
SVG Web ELements
------------------
This is not located by traditional Xpath
//tagname[@attribute='value'] ==> for none svg element locator

E.g
BoilerPlate Code
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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Login Steps
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

'''
To locate svg element one needs to follow:
//*[name()='svg']
* represents all web element names
//*[local-name()='svg']
E.g
'''

# Traditional Xpath Locator
# driver.find_element(By.XPATH, "//button[@title='My Timesheet']").click() # PASSED

# Using plain SVG
# driver.find_element(By.XPATH, "//button[@title='My Timesheet']//svg").click() # FAILED

# Xpath with Name()
# driver.find_element(By.XPATH, "//button[@title='My Timesheet']//*[name()='svg']").click() # PASSED

# Xpath with Local-Name()
driver.find_element(By.XPATH, "//button[@title='My Timesheet']//*[local-name()='svg']").click() # PASSED


