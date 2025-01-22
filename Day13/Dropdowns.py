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

drop_down_element = driver.find_element(By.XPATH, "//select[@id='country']") # using 'select' as tag name
# It's import to Select element whenever dropdown element is use
drop_down = Select(drop_down_element) # there are lots of variables to access in the Select class
# One of the method of Select is 'visible text'
# drop_down.select_by_visible_text("United Kingdom")
'''
Output works as expected for UK
'''
# drop_down.select_by_value("australia")
'''
Output works as expected for Aussie
'''
drop_down.select_by_index(3) # Selecting 3 as Germany index number by counting from 0123 of which Germany is on 4th line
# However, the above code in line 35 for index isn't advisable to use
alloptions = drop_down.options
print(len(alloptions))
for option in alloptions:
    print(option.text)

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

driver.quit()