'''
Refer to Handle_Browser_Windows.png file for full notes on this topic

Handle Browser Windows

Browser is responsible to generate unique window ID

E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)

# Open first url and interact  with elements
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Lenovo").click()
driver.find_element(By.LINK_TEXT, "Lenovo").send_keys(Keys.CONTROL+Keys.RETURN)
'''
Output is
Both web pages work as expected
'''