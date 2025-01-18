'''
Authentication Popup
---------------------
- Sometimes when launching an application it will ask for username and password until unless we enter username and password
the page will not appear. This is called Authentication Popup.
- It is not a part of the application (web element) but an additional window imposed on top of the application.
- Companies intentionally introduce these authenticated pop ups before accessing applications to check whether you are a
right person or not. Even send_keys method also will not work.

How to handle Authentication Popup?
--------------------------------------
1. Injection ==> is Bypassing username and password from url itself
http://username:password@the-internet.herokuapp.com/basic_auth
http://admin:admin@the-internet.herokuapp.com/basic_auth
E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
# Validation
msg = driver.find_element(By.TAG_NAME, "p").text
if "Congratulations" in msg:
    print("Login Test Passed")
else:
    print("Login Test Failed")
'''
Output is 
Login Test Passed
'''
