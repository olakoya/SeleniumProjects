'''
Commands in Selenium Webdriver
------------------------------
They are also called methods

Types of Commands
------------------
1. Application Commands: This is the commands that works on applications and they are also known as application methods.

    Different types of Application Commands are:
    --------------------------------------------
    i. Get method () ==> This is use to open application url
    ii. Title method () ==> This returns title of a webpage
    ii. Current _url () ==> This will capture or return current url of a webpage
    iv. Page_source () ==> This will capture tge source code of the webpage
    v. Current_window_handle ==> This will return id of the current browser window
    vi. Window_handles ==> This will return ids of all current opened windows

2. Browser Commands: Browser is responsible to generate an id.

    Different types of Browser Commands are:
    --------------------------------------------
    i. Close method () ==> This is to close single browser window (where driver focused) i.e., parent window
    ii. Quit method () ==> This is the close multiple browser windows (this will kill the process)

E.g
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By # 'by' is a module and inside it we have a class 'By'
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://testautomationpractice.blogspot.com/") # driver.get helps to easily open url application
driver.maximize_window() # this is use to expand the url page to fullscreen by using a 'driver' variable
driver.implicitly_wait(10) # To avoid some exceptions implicit wait is used

print(driver.title)# title method will return command
print(driver.current_url)
print(driver.page_source)
print((driver.current_window_handle))

'''
Output is
1. Url title page: Automation Testing Practice
2. Window id: E9AE2A37AC2C2B6ADE47FCEC93EE706C
e.t.c.
Below is some of the real output but due to the large output it's impossible to paste it here

Automation Testing Practice
https://testautomationpractice.blogspot.com/
<html class="v2" dir="ltr" lang="en"><head>
<link href="https://www.blogger.com/static/v1/widgets/3566091532-css_bundle_v2.css" rel="stylesheet" type="text/css">
<meta content="width=1100" name="viewport">
<meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
<meta content="blogger" name="generator">
<link href="https://testautomationpractice.blogspot.com/favicon.ico" rel="icon" type="image/x-icon">
<link href="https://testautomationpractice.blogspot.com/" rel="canonical">
...............

One can obtain a window id by using the Window_Handles Method
'''

driver.switch_to.new_window("window")
driver.get("https://www.facebook.com/")

# One can obtain a window id by using the Window_Handles Method
print(driver.window_handles)

'''
Output is displaying window ids from both Automation Testing Practice webpage and Facebook
['60FFDCB9AFF428C64EE7B70C26D7C92B', '2BCDF333680E61CBA49D5E52E0DEFEA8']
'''

time.sleep(5)
# driver.close()
driver.quit()

