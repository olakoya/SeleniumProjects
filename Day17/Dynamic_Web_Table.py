from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import none_of

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

nosofrows = driver.find_elements(By.XPATH, "//table[@aid='taskTable']/tbody/tr")
print(len(nosofrows))
'''
Output is 
7
4
Javascript
Learn Selenium Amit Selenium 300 
Learn Java Mukesh Java 500 
Learn JS Animesh Javascript 300 
Master In Selenium Mukesh Selenium 3000 
Master In Java Amod JAVA 2000 
Master In JS Amit Javascript 1000 
Learn Selenium   Selenium   300
Learn Selenium   Selenium   300
Learn Selenium   Selenium   300
Learn Selenium   Selenium   300
Learn Selenium   Selenium   300
Master In JS   Javascript   1000
0
'''
cpu_load = None
# look through rows to find "Chrome" and verify CPU load
for r in range(1, len(nosofrows)+1):
    name = driver.find_element(By.XPATH, "//table[@id='taskTable']//tr["+str(r) + "]/td[1]").text
    if name == "chrome":
        cpu_load = driver.find_element(By.XPATH, "//td[text()='Chrome']//following-sibling::td[contains(text(),'%')]").text
        print(cpu_load)
value = driver.find_element(By.XPATH, "//div[@id='displayValues']/p/strong").text
print(value)
assert value == cpu_load, "Validation Not Successful"
'''
Output is
 File "/Users/olakoya/Desktop/Selenium/Day17/Dynamic_Web_Table.py", line 47, in <module>
    assert value == cpu_load, "Validation Not Successful"
AssertionError: Validation Not Successful
5.5%
'''