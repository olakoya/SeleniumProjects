'''
Full notes can be found in Day 7 (24. WebDriver Waiting Strategies.pdf)

Waiting Strategies
----------------------
time.sleep (10)
exception

Webdriver Waiting Strategies
-----------------------------
implicit_wait (10)
exception
If implicit wait is declared at the beginning then it will take care of all the statements after that implicit wait

Explicit_Wait
--------------
Dynamic wait isn't based on time
And only applies to specific webelement.
It can only be used for certain conditions
With the help of the 'webdriverwait' class we can implement explicit wait

1. Declaration
    WebDriverWait() ==> Passing a parameter which is an argument
    Class consists of a constructor and class is WebDriverWait()
    Driver is a parameter and an instance
    mywait is the object reference
    Explicit wait is used to find element method
Wait until email text box is displayed on the webpage

2. Usage
    mywait.until(EC.visibility_of_element_located((By.ID , "box000"))) ==> this is when the id selector can't be found on the webelement

E.g
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
driver.maximize_window()

mywait = WebDriverWait(driver, 10)  # Declaration of explicit wait
driver.find_element(By.ID , "adder").click()
# red_box = driver.find_element(By.ID , "box0")

red_box = mywait.until(EC.visibility_of_element_located((By.ID , "box0")))
print(red_box.is_displayed())

'''
Output is error due to wrong locator however the explicit wait timed out after 10seconds when id locator "box000"isn't found
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message: 

Output for an accurate id selector 'box0' is
True
'''