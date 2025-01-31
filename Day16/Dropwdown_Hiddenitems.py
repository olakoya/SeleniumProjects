from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
driver.maximize_window()

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

driver.find_element(By.XPATH, "//span[text()='PIM']").click()
driver.find_element(By.XPATH, "//label[text()='Job Title']//following::div[1]").click()

all_options = driver.find_elements(By.XPATH, "//div[@role='option']//span")
print(len(all_options))

for option in all_options:
    # print(option.text)
    if option.text == "QA Lead":
        option.click()
        break
'''
Output is 
28
Account Assistant
Automaton Tester
Chief Executive Officer
Chief Financial Officer
Chief Technical Officer
Content Specialist
Customer Success Manager
Database Administrator
Finance Manager
Financial Analyst
Head of Support
HR Associate
HR Manager
IT Manager
Network Administrator
Payroll Administrator
Pre-Sales Coordinator
QA Engineer
QA Lead
qwer
rsjsrii
Sales Representative
Social Media Marketer
Software Architect
Software Engineer
Support Specialist
VP - Client Services
VP - Sales & Marketing


Output after adding lines 28 to 31
28
'''

# driver.close()