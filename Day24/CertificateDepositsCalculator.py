import time

import XLUtils
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
driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
driver.maximize_window()
driver.implicitly_wait(10)

# Accepting Cookies on Page
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

# Elements
inideposit = driver.find_element(By.XPATH, "//input[@id='mat-input-0']")
length = driver.find_element(By.XPATH, "//input[@id='mat-input-1']")
apr = driver.find_element(By.XPATH, "//input[@id='mat-input-2']")
# calbutton = driver.find_element(By.XPATH, "//button[@id='CIT-chart-submit']")

path = r"/Users/olakoya/Desktop/Selenium/Day24/caldata.xlsx"
rows = XLUtils.getRowCount(path, "Sheet1")
print(f"Total rows: {rows}")

for r in range(2, rows + 1):
    inidepo = XLUtils.readData(path, "Sheet1", r, 1)
    interestrate = XLUtils.readData(path, "Sheet1", r, 2)
    monthlength = XLUtils.readData(path, "Sheet1", r, 3)
    compoundingmonths = XLUtils.readData(path, "Sheet1", r, 4)
    exptotal = XLUtils.readData(path, "Sheet1", r, 5)

# Clearing Existing Data
    inideposit.clear()
    length.clear()
    apr.clear()
    time.sleep(3)

# Send or Entering Data
    inideposit.send_keys(inidepo)
    length.send_keys(monthlength)
    apr.send_keys(interestrate)

# Handling Dropdown
    compoundrp = driver.find_element(By.XPATH, "//mat-select[@id='mat-select-0']")
    compoundrp.click()
    time.sleep(3)

# Select the Dropdown Value
#     options = driver.find_elements(By.ID, "mat-option-1")
#     for option in options:
#         if (option.text == compoundingmonths):
#             option.click()
#     calbutton.click()

    option_xpath = f"//mat-option//span[contains(text(), '{compoundingmonths}')]"
    driver.find_element(By.XPATH, option_xpath).click()

    # Wait for the button to be clickable and click it
    calbutton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='CIT-chart-submit']"))
    )
    calbutton.click()

# Wait for the Result to be Visible
#     acttotal = driver.find_element(By.ID, "displayTotalValue").text

    acttotal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "displayTotalValue"))
    ).text

    print("Expected total is from excel: ", exptotal)
    print("Expected total is from webpage: ", acttotal)

    # Validation
    if exptotal == acttotal:
        assert True, "Test Case Passed"
    else:
        assert False, "Test Case Failed"

print("Calculation has been completed.")
driver.close()

'''
Output is
Sheet2 already exists.
Data written and workbook saved successfully.
Total rows: 7
Expected total is from excel:  $520.39
Expected total is from webpage:  $520.39
Expected total is from excel:  $1,083.14
Expected total is from webpage:  $1,083.14
Expected total is from excel:  $1,623.65
Expected total is from webpage:  $1,623.65
Expected total is from excel:  $3,244.89
Expected total is from webpage:  $3,244.80
Traceback (most recent call last):
  File "/Users/olakoya/Desktop/Selenium/Day24/CertificateDepositsCalculator.py", line 87, in <module>
    assert False, "Test Case Failed"
AssertionError: Test Case Failed
'''