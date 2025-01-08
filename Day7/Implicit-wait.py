
'''
Wait commands in Selenium Webdriver are:
-----------------------------------------
1. Implicit wait
2. Explicit wait
3. Fluent wait

'''
from selenium import webdriver
from selenium.webdriver.common.by import By # 'by' is a module and inside it we have a class 'By'
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.selenium.dev/selenium/web/dynamic.html") # driver.get helps to easily open url application
driver.maximize_window()
driver.implicitly_wait(3) # this comes from selenium (if element is available it could execute for 1 second unlike time.sleep will wait for 3 seconds
driver.find_element(By.ID , "adder").click()
red_box = driver.find_element(By.ID , "box0")
print(red_box.is_displayed())

'''
Output is
True
'''