'''
4. Navigational Commands: This is moving from one point to another that is, will control browser navigation

     Different types of Navigation Commands are:
    --------------------------------------------
    i. Back method () ==> This is to go to the previous page in the browser history. It's same as "back" button in the browser.
    ii. Forward method () ==> This is to go to the next page in the browser history. It's same as "Forward" button in the browser.
    iii. Refresh method () ==> This reloads the current page. It's same as the "Refresh" button in the browser.
E.g
'''
import time

from attr.validators import max_len
from selenium import webdriver
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.ebay.com/") # driver.get helps to easily open url application

time.sleep(3)

driver.get("https://www.myntra.com/")

time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()

driver.quit()
'''
Output is
Works as expected
'''

'''
5. Wait Commands:

'''