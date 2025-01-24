'''
Dropdown 2
-----------
Dropdown with Input box
Sorted Dropdown

Rama
Ram

E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Approach 1
# country_dropdown_element = driver.find_element(By.ID , "billing_country")
# country_dropdown = Select(country_dropdown_element)
# alloptions = country_dropdown.options
# print(len(alloptions))
'''
Output works as expected ==> Billing Country 'UK' was selected and is
250
'''
# country_dropdown.select_by_visible_text("Belarus")
'''
Output didn't work as expected ==> Billing Country remains UK - FAILED and is 
250
'''

# for option in alloptions:
#     if option.text == "Belarus":
#         option.click()
#         break
'''
Output works as expected ==> Billing Country 'Belarus' was selected and is
250
'''

# Approach 2
# driver.find_element(By.XPATH , "//span[@aria-label='Country']//span[@role='presentation']")
# alloptions = driver.find_elements(By.XPATH, "//select[@name='billing_country']//option")
# print(len(alloptions))
# for option in alloptions:
#     if option.text == "Spain":
#         option.click()
#         break
'''
Output works as expected ==> Billing Country 'Belarus' was selected and is
250

When 'Spain' was added to line 51 
Output works as expected ==> Billing Country 'Spain' was selected and is
250
'''

# Approach 3
# driver.find_element(By.XPATH , "//span[@aria-label='Country']//span[@role='presentation']").click()
# driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys("Georgia", Keys.ENTER)
'''
Output works as expected ==> Billing Country 'Spain' was selected and is
Output works as expected ==> Billing Country 'Georgia' was selected and is
'''

# Approach 4
driver.find_element(By.XPATH , "//span[@aria-label='Country']//span[@role='presentation']").click()
# driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys("Gree", Keys.ENTER)
'''
Output works as expected ==> Billing Country 'Greece' was selected and is
'''
driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys("Gree")
driver.find_element(By.XPATH, "//ul[@id='select2-billing_country-results']//li[2]").click()
'''
Output works as expected ==> Billing Country 'Greenland' was selected and is
'''



# driver.close()
# driver.quit()