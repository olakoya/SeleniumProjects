'''
Locators in Selenium Webdriver
--------------------------------
Every web applications have elements.
And every element contains action that's performed
And the element can be validated
House address is what one calls location
And the letter sent to the house address that is location is called an action
We need to locate the element to perform action on it

Locators are called addresses of web elements
Every web elements has  a location
We need locators because with the help of web element we can perform some actions

In another word we need locators to identify web element on web page
And to perform some action on that web element
And to perform action on this web element we need a locator

We have different types of locators
------------------------------------
1. Basic or Normal Locators or Locators
    i. Id
    ii. Name
    iii. Linktext or Partial Linktext
    iv. Class Name
    v. Tage Name

2. Customized Locators
    a. Css Selector
    b. XPath

2a. CSS Selector
----------------
i. Tag and ID
ii. Tag and Class
iii. Tag and Attribute
iv. Tag, Class and Attribute

2b. XPath
-----------
i. Absolute XPath
ii. Relative XPath

Every web (frontend) application will be designed by some codes which are HTML, CSS, Javascript
To know the details of an element we need to observe HTML code of the webpage

Steps to take are:
-------------------
1. Right Click anywhere on the page and click on inspect button or ctrl+shift+i
2. Developer tools is what the page is called and it opens and element tab will showcase the html and css codes
3. Click on selector icon to move around
4. For each and every web element we need to locate the html line and it becomes highlighted in Blue when the mouse hoover over it
5. To write a locator one will look at the html line and at the beginning, tag-name is displayed followed at the attribute then attribute Value
6. Attribute is nothing but a property and a dedicated value.

Every element in the html line is having a tag-name
along with Tag-name is having multiple attributes which are properties
Each attribute is having certain value

input => Tag-name
type => Attribute/Property
id => Attribute/Property
Value name => Attribute/Property

Values can have duplicates but no attributes or properties name will be duplicates as seen below

<div            type="testvalue"                    name="testvalue"                    div>
tagname   attributename=attributevalue      attributnamee=attributesvalue              tagname

Attribute names can't be duplicate but attribute values and tag-names can be duplicate as seen above
You can view common HTML tags by clicking the attached screenshot names "CommonHTMLTagNames" from png files to the left
Multiple elements have more tags

Types of Basic Locators are;
----------------------------
1. ID
2. NAME
3. CLASS NAME
4. LINKTEXT
5. PARTIAL LINKTEXT
6. TAGNAME

<input type="text" id="twotabsearchtextbox" value="" name="field-keywords" autocomplete="off" placeholder="Search Amazon.co.uk"
 class="nav-input nav-progressive-attribute" dir="auto" tabindex="0" aria-label="Search Amazon.co.uk" role="searchbox" aria-aut-
 ocomplete="list" aria-controls="sac-autocomplete-results-container" aria-expanded="false" aria-haspopup="grid" spellcheck="fals
e">

ID Locator Strategy: If a html link has id locator value as seen as above html link to locate the element e.g id="twotabsearchtextbox"
NAME Locator Strategy: Is by locating the element with a name value e.g name="field-keywords"
CLASSNAME Locator Strategy: Class without a name is what will be found e.g class="nav-input nav-progressive-attribute"
LINKTEXT Locator Strategy: If it's Link, it will always have a link text. As seen below link 'a' is always a tag name
<a href="/ref=nav_logo" id="nav-logo-sprites" class="nav-logo-link nav-progressive-attribute" aria-label="Amazon.co.uk">
      <span class="nav-sprite nav-logo-base"></span>
      <span id="logo-ext" class="nav-sprite nav-logo-ext nav-progressive-content"></span>
      <span class="nav-logo-locale">.co.uk</span>
    </a>

PARTIAL LINKTEXT Locator Strategy: This has a text that its visible name on the web page can be seen in the link as seen
on the html line below html e.g >Log in</button>
<button value="1" class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy" name="login" data-testid="royal_login_button"
type="submit" id="u_0_5_38">Log in</button>

And because it is a link text one would see the text in double quotations e.g >Create new account</a>

<a role="button" class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy" href="/r.php?entry_point=login" ajaxify="" id="u_0_0_zU"
 data-testid="open-registration-form-button">Create new account</a>

TAGNAME Locator Strategy: Element can also be located by using tag-name e.g <a role="button"

TAG NAMES AND CLASS NAME rae used to locate multiple web elements

E.g
'''

# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# # creating a chromebrowser instant
#
# driver = webdriver.Chrome(options=options) # with the help of chrome(options) instance, driver is variable
# # with the help of instance one can call the method of the class
# # Methods are use to preform action on the web element on the web page once a locator is specify
# # So with the help og driver all the methods in the class will be called

# driver.get("http://www.automationpractice.pl/index.php")
# driver.maximize_window()


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
driver.get("http://www.automationpractice.pl/index.php")
print("Navigated to the website")
driver.maximize_window()

'''
To perform some more actions in the web element one needs to use 'find_element(Locator or Address of the element)' method
by using any of the basic locators strategies
One needs to add (from selenium.webdriver.common.by import By) to line 131 above

'''
# we are importing the 'By' class to strategies the below strategy
# ID
driver.find_element(By.ID, "search_query_top").send_keys("T-shirts")
print("Typing in the search box")
# Name
driver.find_element(By.NAME, "submit_search").click()
print("Clicking the search button")

# LINK/PARTIAL LINK TEXT
# driver.find_element(By.LINK_TEXT, "Printed Chiffon Dress").click()
# print("Search item selected")

driver.find_element(By.PARTIAL_LINK_TEXT, "Printed Chiffon Dress").click()
print("Search item selected")

# to enter a text one needs to use a 'send_keys()' method and for click action will use 'click()' method and clear for 'clear()'
# Add your test logic here
driver.close()

'''
Output is
Navigated to the website
Typing in the search box
Clicking the search button
Search item selected
'''