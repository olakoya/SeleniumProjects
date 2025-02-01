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

# Operations on Webtable
nosofrows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
# nosofcols = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")
nosofcols = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[2]/td")
print(len(nosofrows))
print(len(nosofcols))

'''
Output is
7
4
'''

# Read a Specific Row and Column Data
data = driver.find_element(By.XPATH, '//table[@name="BookTable"]//tr[7]/td[3]').text
print(data)

'''
Output is
7
4
1000

Output after changing line 31 [4] to [3]
Javascript
'''

# Read All Rows and Column Datas
for r in range(2,len(nosofrows)+1):
    for c in range(1,len(nosofcols)+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text # using dynamic xpath
        print(data, end= " ")
    print()

'''
Output is
7
4
Javascript
Learn Selenium
Amit
Selenium
300
Learn Java
Mukesh
Java
500
Learn JS
Animesh
Javascript
300
Master In Selenium
Mukesh
Selenium
3000
Master In Java
Amod
JAVA
2000
Master In JS
Amit
Javascript
1000


Output after adding (end= " ") to line 48
7
4
Javascript
Learn Selenium Amit Selenium 300 Learn Java Mukesh Java 500 Learn JS Animesh Javascript 300 Master In Selenium Mukesh Selenium 3000 Master In Java Amod JAVA 2000 Master In JS Amit Javascript 1000 


Output after adding 'print()' in line 49
7
4
Javascript
Learn Selenium Amit Selenium 300 
Learn Java Mukesh Java 500 
Learn JS Animesh Javascript 300 
Master In Selenium Mukesh Selenium 3000 
Master In Java Amod JAVA 2000 
Master In JS Amit Javascript 1000 
'''


driver.quit()