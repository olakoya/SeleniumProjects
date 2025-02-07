'''
Shadow DOM (Document Object Model) Elements
--------------------------------------------
- Browser is responsible to generate DOM
- DOM shadow DOM ==> that is found in main DOM
- Encapsulate means hiding original functionality
- This can be found in HTML only
- Isolation style and behaviour concepts


What is Shadow Host?
-----------------------

- This is regular DOM element
- This  is shadow DOM is attached


Shadow Tree
-----------
- Is Shadow root and Shadow DOM element


Shadow Root
------------
- This is a parent of shadow DOM Element


Shadow Boundary
---------------
Shadow DOM and Regular DOM


DOM consists of ==> Shadow Host (Regular DOM Element) consists of ==> Shadow Root consists of ==> Shadow DOM Element


==> Xpath will never work on Shadow Element

CSS Selectors
    tagname + value of id attribute ==> tagname#valueofIdattribut
    tagname + value of class attribute ==> tagname.valueofclassattribute
    tagname + attribute ==> tagname[attribute=value]
    tagname + class + attribute ==> tagname.value of class attribute[attribute=value]

E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://dev.automationtesting.in/shadow-dom")
driver.maximize_window()

# Shadow Element
#------------------
# Shadow Host
# shadow_host = driver.find_element(By.XPATH, "//div[@id='shadow-root']")
#
# # Shadow Root
# # shadow_root = shadow_host.shadow_root
#
# shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
#
# # shadow_element = shadow_root.find_element(By.XPATH, "//div[@id='shadow-element']")
# shadow_element = shadow_root.find_element(By.CSS_SELECTOR, "#shadow-element")
# print(shadow_element.is_displayed())
'''
Output is
True
'''

'''
Shadow DOM Selectors
-----------------------


Executing Javascript Statement
-------------------------------

'''

# Nested Shadow Element
#------------------------

# shadow_host_1 = driver.find_element(By.XPATH, "//div[@id='shadow-root']")
# shadow_root_1 = shadow_host_1.shadow_root
# shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR, "#inner-shadow-dom")
# shadow_root_2 = shadow_host_2.shadow_root
# shadow_element = shadow_root_2.find_element(By.CSS_SELECTOR, "#nested-shadow-element")
# print(shadow_element.is_displayed())
'''
Output is 
True
'''

# Multi Nested Shadow Element
#-----------------------------

shadow_host_1 = driver.find_element(By.XPATH, "//div[@id='shadow-root']")
shadow_root_1 = shadow_host_1.shadow_root
shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR, "#inner-shadow-dom")
shadow_root_2 = shadow_host_2.shadow_root
shadow_host_3  = shadow_root_2.find_element(By.CSS_SELECTOR, "#nested-shadow-dom")
shadow_root_3 = shadow_host_3.shadow_root
shadow_element = shadow_root_3.find_element(By.CSS_SELECTOR, "#multi-nested-shadow-element")
print(shadow_element.is_displayed())
'''
Output is 
True
'''