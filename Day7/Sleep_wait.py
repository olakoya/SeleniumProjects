'''
Automation Script ==> This is executed on Web application i.e. to interact with web elements that the web app contains
It is also very fast, web elements get loaded when it's execute
Sometimes web elements to load due to network or other issues and this leads to the script to execute falsely due to slow loading
The above is called SYNCHRONIZATION PROBLEM!

In Automation Testing, we use waiting strategies to make applications under test and the test Automation Tool wokr in parallel.
- Sometimes instead of using wait commands we use python's time module

time.sleep(time in seconds)
==> to continue click on the png file
E.g
'''
import time # this comes from python
from selenium import webdriver
from selenium.webdriver.common.by import By # 'by' is a module and inside it we have a class 'By'
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.selenium.dev/selenium/web/dynamic.html") # driver.get helps to easily open url application
driver.maximize_window() # this is use to expand the url page to fullscreen by using a 'driver' variable

'''
Output is
Web page displays as expected
'''

# click of the box
driver.find_element(By.ID , "adder").click()
time.sleep(3) # waiting for 3 seconds

'''
Output is
A red box is displayed on the web page after clicking
'''

red_box = driver.find_element(By.ID , "box0")
print(red_box.is_displayed())

# using time.sleep(award a time here) this is for syntax and one needs to add import time at the top then add line 36

driver.quit()

'''
Output is 
True
'''

# Below is chatgpt code and above is mine but do the same thing
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Initialize the driver with options
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opt)
#
# # Open the URL
# driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
# driver.maximize_window()
#
# # Click the "Add Element" button
# driver.find_element(By.ID, "adder").click()
#
# # Wait for the red box to appear
# wait = WebDriverWait(driver, 10)  # Timeout after 10 seconds
# red_box = wait.until(EC.presence_of_element_located((By.ID, "box0")))
#
# # Check if the red box is displayed
# print(red_box.is_displayed())
#
# # Close the browser
# driver.close()
'''
Output is 
True
'''

# As an automation tester you are not allowed to use the time.sleep except the developer only
# The time import is only available to the python programming alone

