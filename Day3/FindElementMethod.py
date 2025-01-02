'''

Find element(locator)
Find elements(locator)

Both elements take arguements as locators
Locator is an address that is used to locate web elements to perform some actions

There are some cases that a locator can locate multiple elements e.g inspect a webpage and search element (//h2) the
output will display total number of the particular word on the page

There are 3 types of Scenarios and they can be found in the FindElement.png file in the Day3 directory

Tags and class names are used to locate web elements most of the time

Most of the time class attribute value will be the same for multiple elements

E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By # 'by' is a module and inside it we have a class 'By'
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()

# Create the Service object
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with Service and options
driver = webdriver.Chrome(service=service, options=options)

# Perform your tasks
driver.get("http://www.automationpractice.pl/index.php")
print("Navigated to the website")
driver.maximize_window()

# class locator strategy
# sliders_count = driver.find_elements(By.CLASS_NAME, "homeslider-description")
# print(len(sliders_count))
#
# for ele in sliders_count:
#     print(ele.text)
#
# driver.close()

'''
Output is 
Navigated to the website
5

2nd Output after adding lines 44 & 45
Navigated to the website
5

EXCEPTEUR
OCCAECAT
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin tristique in tortor et dignissim. Quisque non tempor leo. Maecenas egestas sem elit
SHOP NOW !
'''

# counting all the list in the webpage
links_count = driver.find_elements(By.TAG_NAME, "a")
print(len(links_count))

for ele in links_count:
    print(ele.text)

'''
Output is
Navigated to the website
88

2nd output after adding lines 68 & 69
Navigated to the website
88

Sign in
Contact us

Cart (empty)

WOMEN

DRESSES

T-SHIRTS
BLOG

Prev
Next

POPULAR
BEST SELLERS

Women

Our stores
Terms and conditions of use
About us
Ecommerce software by PrestaShop™
My account
My orders
My credit slips
My addresses
My personal info
sales@yourcompany.com
'''

