'''
Javascript Alerts or Popups
----------------------------
- These are Warnings, Confirmations, Prompt(input from a data) user for inputs and they are part of functionality
- It's server responsibility to approve the alert
- Alerts are not webelements, they are web objects
- It's impossible to inspect

Types of Alerts
-----------------
1. Simple Alert: This displays a message abd has an 'ok' button.
2. Confirmation Alert: This displays a message with 'ok' and 'cancel' buttons.
3. Prompt Alert: This displays a message and in input text box, along with 'ok' and 'cancel' buttons.

Commands to handle Alerts
--------------------------
1. myalert = driver.switch_to.alert ==> this will switch to Active Alert in the webpage
2. myalert.text ==> this retrieves text from the Alert
3. myalert.accept ==> this is clicking on 'ok' button
4. myalert.dismiss ==> this will click on cancel button
5. myalert.send_keys() ==> this will send texts to prompt alert
E.g
'''
from idlelib.run import MyHandler

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Prompt Alert
driver.find_element(By.ID, "promptBtn").click()
'''
Output is
Prompt alert popup box was displayed
'''
#
# myalert = driver.switch_to.alert
# print(myalert.text)
# '''
# Output is
# Please enter your name:
# '''
#
# myalert.send_keys("Ola")
# myalert.accept()
# # myalert.dismiss()
# '''
# Output displays as expected
# '''
#
# # Validation
# msg = driver.find_element(By.ID, "demo").text
# assert "Ola" in msg
# '''
# Output is
# Please enter your name:
# '''

# Alerts Handling Using Explicit Wait (EXAM QUESTION)
my_wait = WebDriverWait(driver, 10) # my_wait is variable name
myalert = my_wait.until(EC.alert_is_present())
print(myalert.text)
myalert.send_keys("Ola")
myalert.accept()

# # Validation
msg = driver.find_element(By.ID, "demo").text
assert "Ola" in msg
'''
Output is
Please enter your name:

Meaning "myalert.send_keys("Ola")" is passed
'''

# driver.quit()