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
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.get("https://www.amazon.com/")
# driver.get("https://www.facebook.com/")
# driver.get("https://www.ebay.com/")
# driver.get("https://www.gumtree.com/")
# driver.get("https://dengro.com")
driver.maximize_window()

cookies = driver.get_cookies()
print(len(cookies))

'''
Output for https://testautomationpractice.blogspot.com/ is
0

Output for https://www.amazon.com/ is
8

Output for https://www.facebook.com/ is
0

Output for https://www.ebay.com/ is
8

https://www.gumtree.com/
12

("https://dengro.com")
5

'''


driver.close()