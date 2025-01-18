'''
Notification Popups / Notification Alerts / Browser-Level Notifications
--------------------------------------------------------------------------
- These are like push notifications, browser-specific.
- To disable we need to do some settings at the browser level like ChromeOptions(), EdgeOptions() etc.
E.g
'''

from selenium import webdriver
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://www.justdial.com/")
driver.maximize_window()

'''
Output is
Webpage displayed as expected without a notification
'''