'''
Keyboard Actions
-----------------
Keys()
Select All ---> ctrl + a
Copy means ---> ctrl+c
Paste means ---> ctrl + v
Tab means ---> Tab

To simulate user needs keys and this key class () needs to be imported

pyautogui means automating moments
pyperclip() means ---> copy

'''
# Boiler Codes are reused to begin the code lines i.e. importing libraries from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=en-uk")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

act = ActionChains(driver) # act is object reference variable

input_box_1 = driver.find_element(By.NAME, "input1").send_keys("Ticket")

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
