# Boiler Codes are reused to begin the code lines i.e. importing libraries from selenium

import pyautogui, pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=en-uk")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://www.foundit.in/upload")
driver.maximize_window()

file1 = r"'/Users/olakoya/Desktop/Covering Letters/OlaKoya-CoverLetter.docx'"

# driver.find_element(By.XPATH, "//div[contains(text(),'Upload Resume')]").click()

# Wait for the cookie popup to appear and handle it
try:
    # Example of clicking the accept button
    accept_button = driver.find_element(By.CLASS_NAME, 'fc-button-label')
    accept_button.click()
except Exception as e:
    print("Cookie popup not found or could not be clicked:", e)

# Wait for the page to reload or the popup to disappear
time.sleep(2)

# Now find and click the "Upload Resume" button
upload_button = driver.find_element(By.XPATH, "//div[contains(text(),'Upload Resume')]")
upload_button.click()

# driver.execute_script("arguments[0],click();", driver.find_element(By.ID, "file-upload"))

driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "file-upload"))

pyperclip.copy(file1)
time.sleep(4)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


# driver.close()