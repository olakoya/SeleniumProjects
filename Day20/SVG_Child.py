'''
Locating a Child in SVG
-------------------------
//*[name()='svg']/*[name()='circle']

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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Locating Circle
# while True:
#     circle = driver.find_element(By.XPATH, "//*[name()='svg']/*[name()='circle']")
#
#     if circle:
#         print("PASS: CIRCLE ELEMENT FOUND SUCCESSFULLY ON THE WEBPAGE!")
#     else:
#         print("FAIL: COULD NOT FIND THE CIRCLE ELEMENT.")
#     break
'''
Output is
PASS: CIRCLE ELEMENT FOUND SUCCESSFULLY ON THE WEBPAGE!
'''

# Locating Polygon
# while True:
#     circle = driver.find_element(By.XPATH, "//*[name()='svg']/*[name()='polygon']")
#
#     if circle:
#         print("PASS: POLYGON ELEMENT FOUND SUCCESSFULLY ON THE WEBPAGE!")
#     else:
#         print("FAIL: COULD NOT FIND THE POLYGON ELEMENT.")
#     break
'''
Output is
PASS: POLYGON ELEMENT FOUND SUCCESSFULLY ON THE WEBPAGE!
'''

# Locating Rectangle
while True:
    circle = driver.find_element(By.XPATH, "//*[name()='svg']/*[name()='rect']")

    if circle:
        print("PASS: RECTANGLE ELEMENT FOUND SUCCESSFULLY ON THE WEBPAGE!")
    else:
        print("FAIL: COULD NOT FIND THE RECTANGLE ELEMENT.")
    break
'''
Output is
PASS: RECTANGLE ELEMENT FOUND SUCCESSFULLY ON THE WEBPAGE!
'''

driver.close()