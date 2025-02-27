import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Elements
inideposit = driver.find_element(By.XPATH, "//input[@id='mat-input-0']")
length = driver.find_element(By.XPATH, "//input[@id='mat-input-1']")
apr = driver.find_element(By.XPATH, "//input[@id='mat-input-2']")
calbutton = driver.find_element(By.XPATH, "//button[@id='CIT-chart-submit']")

path = r"/Users/olakoya/Desktop/Selenium/Day24/caldata.xlsx"

rows = XLUtils.getRowCount(path, "Sheet1")
print(rows)

for r in range(2,rows+1):
    inidepo = XLUtils.readData(path, "Sheet1", r, 1)
    interestrate = XLUtils.readData(path, "Sheet1", r, 2)
    monthlength = XLUtils.readData(path, "Sheet1", r, 3)
    compoundingmonths = XLUtils.readData(path, "Sheet1", r, 4)
    exptotal = XLUtils.readData(path, "Sheet1", r, 5)

# Clearing Existing Data
    inideposit.clear()
    length.clear()
    apr.clear()

# Send or Entering Data
    inideposit.send_keys(inidepo)
    length.send_keys(monthlength)
    apr.send_keys(interestrate)

# Handling Dropdown
    compoundrp = driver.find_element(By.XPATH, "//mat-select[@id='mat-select-0']")
    compoundrp.click()
    options = driver.find_elements(By.XPATH, "//div[@id='mat-select[@id='mat-select-0-panel']//mat-option")
    for option in options:
        if (option.text == compoundingmonths):
            option.click()