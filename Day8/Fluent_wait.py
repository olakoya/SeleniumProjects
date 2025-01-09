'''
Fluent Wait Strategy
---------------------
explicit wait and poll frequency is fluent wait
'''

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
driver.maximize_window()

mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         Exception])  # Declaration of explicit wait
driver.find_element(By.ID , "adder").click()
# red_box = driver.find_element(By.ID , "box0")

red_box = mywait.until(EC.visibility_of_element_located((By.ID , "box0")))
print(red_box.is_displayed())