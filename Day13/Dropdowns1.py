'''
Dropdowns notes can be found in Day13 pdf file
Class has different multiple methods e.g select, feature, value, option

list = [1 2 3 4]
Having 0 as index value
E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# # Example 1 ==> Single Selected  Dropdown
# drop_down_element = driver.find_element(By.XPATH, "//select[@id='country']") # using 'select' as tag name
# # It's import to Select element whenever dropdown element is use
# drop_down = Select(drop_down_element) # there are lots of variables to access in the Select class
# # One of the method of Select is 'visible text'
# drop_down.select_by_visible_text("United Kingdom")
'''
Output works as expected for UK
'''
# drop_down.select_by_value("australia")
'''
Output works as expected for Aussie
'''
# drop_down.select_by_index(3) # Selecting 3 as Germany index number by counting from 0123 of which Germany is on 4th line
# # However, the above code in line 35 for index isn't advisable to use
# alloptions = drop_down.options
# print(len(alloptions))
# for option in alloptions:
#     print(option.text)

'''
Output works as expected and displayed list below in terminal
United States
Canada
United Kingdom
Germany
France
Australia
Japan
China
Brazil
India


Output after adding line 38 to print the total length is
10
'''

# assert drop_down.first_selected_option.text == "United Kingdom" # assert is used for validation or assert is validation
'''
Output works as expected 
'''
# if drop_down.first_selected_option.text == "United Kingdom": # If actual(drop_down....) isn't equal to expected(UK) it will 'fail' the action
#     print("Test Passed")
# else:
#     print("Test Failed")
'''
Output works as expected and displays
Test Passed
'''

# Example 2 ==> Multiple Selected Dropdown
drop_down_element = driver.find_element(By.XPATH, "//select[@id='colors']")
drop_down = Select(drop_down_element)
print(drop_down.is_multiple) # True
drop_down.select_by_visible_text("Blue")
drop_down.select_by_value("red")
drop_down.select_by_index(3)
'''
Output works as expected and displays
True
'''

print(drop_down.first_selected_option.text)
'''
Output works as expected and displays
True
Red (this shows that red was selected first)
'''
# Repeating code lines 36 to 41 but for dropdown colors and above one was for countries
all_selected_options = drop_down.all_selected_options
for option in all_selected_options:
    print(option.text)
'''
Output is 
True
Red
Red
Blue
Yellow
Red
'''
# Deselecting Options
# drop_down.deselect_by_visible_text("Blue")
# drop_down.deselect_by_value("red")
# drop_down.deselect_by_index(3)
'''
Output is 
True
Red
Red
Blue
Yellow
Red
'''
# Using the below one single method code to deselect the options unlike the lines of codes in 186 to 108
drop_down.deselect_all()
'''
Output is 
True
Red
Red
Blue
Yellow
Red
'''

# driver.quit()
# driver.close()

'''
One must always import the select tag name 'from selenium.webdriver.support.select import Select' in line 12 before eoe can use the select 
and deselect method
'''

