'''
If it's a bookstrap dropbox/down one would not be able to see the tag name (read more from the notes)

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
driver.get("https://www.jquery-az.com/boots/demo.php?ex=63.0_2")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[contains(@class,'multiselect')]").click()
'''
Output works as expected by selecting HTML and CSS
'''
# html_ele = driver.find_element(By.XPATH,"//input[@value='HTML']")
# print(html_ele.is_selected())
'''
Output works as expected by selecting HTML and CSS and display is
True
'''

# Select a single item
driver.find_element(By.XPATH,"//input[@value='Java' or @value='Python' or @value='Oracle']").click()
'''
Output works as expected by selecting HTML, CSS and Java
'''
# Capture all options from dropdown
all_options = driver.find_elements(By.XPATH,"//ul[contains(@class,'multiselect')]//label")
# print(len(all_options))
# for option in all_options:
#     print(option.text)
'''
Output is
11
'''

for option in all_options:
    if option.text == "Python" or option.text=="Oracle": # If this condition becomes true thr below action will be executed
        option.click()
'''
Output is
Output works as expected by selecting HTML, CSS, Java, Python and Oracle
'''