'''
3. Conditional Commands: This is to check the state of an element

    Different types of Conditional Commands are:
    --------------------------------------------
    i. is_displayed method () ==> To check link if is displayed before clicking on --> Applicable for all elements
    ii. is_enabled Method () ==> To check if the element displayed is enabled in order to interact with it --> Applicable for all elements
    iii. is_selected Method () ==> This is selection based conditional command e.g checkbox, radio button etc --> Only for Checkboxes and Radio buttons

NB: Conditional commands always return a Boolean (True or False) Value
E.g
'''

import time

from attr.validators import max_len
from selenium import webdriver
from selenium.webdriver.common.by import By # 'by' is a module and inside it we have a class 'By'
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://testautomationpractice.blogspot.com/") # driver.get helps to easily open url application
driver.maximize_window() # this is use to expand the url page to fullscreen by using a 'driver' variable
driver.implicitly_wait(10) # To avoid some exceptions implicit wait is used

# interacting with elements (textbox field, checkbox, radio button etc) on the applications

name_txt_box = driver.find_element(By.ID, "name")
print(name_txt_box.is_displayed()) # this is a condition command to check if name text box is displayed on the application
print(name_txt_box.is_enabled()) # this is a condition command to check if name text box is enabled on the application
# name_txt_box.is_selected() # this only applies to checkbox or radio button

'''
Output is
True
True
'''

# this is the select command method
male_rd = driver.find_element(By.ID, "male")
print(male_rd.is_selected()) # conditional command

female_rd = driver.find_element(By.ID, "female")
print(female_rd.is_selected()) # conditional command

time.sleep(3)
male_rd.click()

# this is click command method
male_rd = driver.find_element(By.ID, "male")
print(male_rd.is_selected()) # conditional command

female_rd = driver.find_element(By.ID, "female")
print(female_rd.is_selected()) # conditional command

'''
Output is
True
True
False
False
True
False
'''

