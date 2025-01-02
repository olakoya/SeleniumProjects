'''
Types of Customised Locators
-----------------------------
One can't directly find these locators on the html code and they are;

i. CSS Selectors (To read more about css click on the css.png file on Day3)
ii. XPath

SHADOW DUMB ELEMENT is element that has no attribute and found under shadow-root (open)
The above can be found when inspecting the search box on google page when a new chrome tab is opened

However only css selectors can be used to locate the element in this case of having a shadow dumb element
(refer to the css.png file to read more)

How to write CSS Selectors?
----------------------------
1. Id
2. Class
3. Name
4. Tag name

How to locate a Web Element?
------------------------------
Combining the selectors name to find the web element easily
E.g: Inspecting facebook login page and inspecting it, then copy HTML of the email text box
<input type="text" class="inputtext _55r1 _6luy" name="email" id="email" data-testid="royal_email" placeholder="Email
address or phone number" autofocus="1" aria-label="Email address or phone number">

1. id + Tagname: (#)
-----------------------
tagname#value of the id attribute
            input is tagname
            value is email
Equals ==> input#email (put this in the search text box on the inspect page returns the above html locator"

2. class + Tagname: (.)
------------------------
tagname.vale of the class attribute
            class value is "inputtext _55r1 _6luy"
            input is tagname
==> input.inputtext _55r1 _6luy (But due to spaces inbetween this is an invalid value so we select the text only before the space)
 Equals ==> input.inputtext

 3. attribute + Tagname: ([])
 -----------------------------
 tagname[attribute=value]
            input is Tagname
            class value is type
Equals ==>   input[type=text]

4. class + attribute + Tagname: (combination of nos 2 and 3 above)
------------------------------------------------------------------
tagname.value of the class attribute[attribute=value]
            Tagname is input.inputtext[]
            class value is data-testid="royal_email"
Equals ==> input.inputtext[data-testid=royal_email]

E.g
'''
from selenium import webdriver
from selenium.webdriver.common.by import By # 'by' is a module and inside it we have a class 'By'
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()

# Create the Service object
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with Service and options
driver = webdriver.Chrome(service=service, options=options)

# Perform your tasks
driver.get("https://www.facebook.com/")
# print("Navigated to the website")
driver.maximize_window()

# using nos 4 from the above combined css selectors
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys(("Ola"))