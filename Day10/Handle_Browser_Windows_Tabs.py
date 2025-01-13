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
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Lenovo").click() # click action will open
# driver.find_element(By.LINK_TEXT, "Lenovo").send_keys(Keys.CONTROL+Keys.RETURN) # send keys will open in another tab
'''
Output is
Both web pages work as expected
'''
# Every window has an id
# print(driver.current_window_handle) # command to use to get window id of test automation webpage
'''
Output is window id
FB16D6EFBA1E53FD928ED7838760AF76

2nd execution output is
F1802CD01BBDBD6F5C47A5E5DEDE5A5E
'''

# 2 tabs and 2 window ids in lines 20 and 23
# print(driver.window_handles)
'''
Output is
['56DEE99489249D141D6B4B7950FB928C']

['229DFE5B72714C8AB1792C28B7FB45B8']
'''
# Opening new tabs and windows
# driver.switch_to.new_window("tab")
# driver.switch_to.new_window("window")

# print(driver.window_handles)

'''
Output is
['B61875E492D8B30BE6FB70D808E9C9E7', '1C9B969F9B370B583E8EFC4FFEDDCA25', 'E6F8F9C4DA1B913B18745FC1F3FC226A']
'''

driver.switch_to.new_window("tab")
driver.get("https://www.facebook.com/")
driver.switch_to.new_window("window")
driver.get("https://www.ebay.com/")

window_ids = driver.window_handles
print(window_ids)
'''
Output is from Test Automation, Facebook and Ebay webpages
['7788D6AA97EE1B9E34AB7B48C4A9C7B4', 'B1DAF4190CF9319BC62D767CB462DFF5', 'C7FAFFD801803702A87C0A7C3A29F888']

'''

# Close specific window or tab
for win_id in window_ids:
    driver.switch_to.window(win_id)
    if driver.title == "Lenovo Official UK Site| Laptops, PCs, Smartphones, Data Center | Lenovo UK":
        driver.close()
'''
Output is
['7B9195381272CA0F106A47589541B2FB', 'BBBB30AFDF7FAD4FA912165DFE67A739', '7687A813C70E7DC6A968728D493D2D9C']

'''

# driver.close()
driver.quit()