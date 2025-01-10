'''
Handling Webelements
---------------------

Input Box or Text Box
----------------------
A textbox or an input box is a field in an user interface where users can type and enter text or data.
    i is_displayed ()
    ii. is_enabled ()
    iii. enter text --> send_keys("text")
    iv. clear text --> clear()
E.g
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# text_box = driver.find_element(By.ID, "name")

# How to perform action
# if text_box.is_displayed():
#     if text_box.is_enabled():
#         print("Element is displayed and enabled")
#         text_box.send_keys("Ola")
#         time.sleep(5)
#         text_box.clear()
#         time.sleep(5)
#         text_box.send_keys("Angel")
#         time.sleep(5)
#
# driver.quit()
'''
Output is
Element is displayed and enabled
'''

# Due to having many attributes we want to number of characters into the text box by using 'maxlength' selector from the webelement.

# print(text_box.get_attribute("classsssssssssss"))
# driver.close()
'''
Output for "maxlength" is
15

Output for "class" is
form-control

Output for "classssssssssss" is
None
'''
#-----------------------------------------------
'''
Radio Button
-------------
A radio button is a GUI element that allows to select one option from a set of mutually exclusive options.

Checkbox or Tick box or Selection box
--------------------------------------
A check box or tick box or selection box is an input field provided to the user on a webpage forms which allows them to
select one or more options from a predefined list.

Tagname for all of the above handling webelements input
click() action in the form of method will be implemented
'''
# Examples of Radio button and Checkboxes
# rd_male = driver.find_element(By.ID, "male")
# rd_female = driver.find_element(By.ID, "female")
# print(rd_male.is_selected()) # False
# print(rd_female.is_selected()) # False
# # rd_male.click()
# rd_female.click()
# print(rd_male.is_selected()) # True
# print(rd_female.is_selected()) # True
'''
Output for 'rd_male.click()' is
False
False
True
False

Output for 'rd_female.click()' is
False
False
False
True
'''
#----------------------------------
# Examples of Selecting a specific checkbox
# driver.find_element(By.ID, "monday").click()
'''
Output is 
Works as expected 
'''

# Examples of Selecting all checkboxes by using custom xpath
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes))
'''
Output for len is
7
'''
#--------------------------------
# Approach 1
# for checkbox in checkboxes:
#     checkbox.click()
'''
Output is
All checkboxes were clicked
7
'''
# Approach 2
'''
Range generates list
[a, b, c, d, e]
a --> 0
b --> 1
c --> 2
d --> 3
e --> 4

x[2] --> c

Monday --> 0
Tuesday --> 1
Wednesday --> 2
Thursday --> 3
Friday --> 4
Saturday --> 5
Sunday --> 6

range of checkboxes = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
range(10) --> 0 to 9
range(20) --> 0 to 19

range(7) --> 0 to 6
range(len(checkboxes)) --> 0 to 6

for i in range(len(checkboxes)):
        checkboxes[i]
'''
# for i in range(len(checkboxes)):
#         checkboxes[i].click()
'''
Output is
All checkboxes were checked
7
'''
#-------------------------------------------

time.sleep(3)
# Example of Clearing all the checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()
'''
Output is
All checkboxes were checked and unchecked
7
'''
#---------------------------------------------
# Selecting multiple checkboxes based on choice
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute("id")
#     if weekname == "tuesday" or weekname == "thursday":
#         checkbox.click()
'''
Output is
Selected checkboxes were checked
7
'''
#-------------------------------------------------------
# Selecting First 2 checkboxes
# for i in range(len(checkboxes)):
#     if i<4:
#         checkboxes[i].click()

'''
Output is
Selected checkboxes were checked
7
'''
#-------------------------------------------------------
# Selecting last 2 checkboxes
'''
range(5) --> 0 to 4
range(4,100) --> 4 to 99
range of checkboxes = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
                        0         1         2          3        4       5         6
range(5,7) --> 5 to 6
range(len(checkboxes)-2,7)
range(len(checkboxes)-2,len(checkboxes))
range(len(checkboxes)-3,len(checkboxes))
'''
# for i in range(len(checkboxes)-2,len(checkboxes)):
#         checkboxes[i].click()
'''
Output is 
Last 2 checkboxes were checked 
7
'''
# Selecting last 3 checkboxes
for i in range(len(checkboxes)-3,len(checkboxes)):
        checkboxes[i].click()
'''
Output is 
Last 3 checkboxes were checked 
7
'''
# driver.close()
# driver.quit()