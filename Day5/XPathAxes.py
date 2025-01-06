'''
Basic Locators are;
    ID, NAME, CLASS, TAGNAME, LINKTEXT, PARTIALLINKTEXT

Customised Locators are;
    CSS SELECTORS
    XPATH
        Relative Xpath
        Absolute Xpath

Every element in the HTML has a tagname in the HTML line.
Every element ....... has a certain attributes
Every element ........ has certain value
With the help of the attribute value we can locate an element by using locator strategies

tr in html is a tagname
tr has no attribute

Scenario - 1
-------------
Supposing an element is not having aany attributes, how can we locate this element?
Answer: Is by using any of the basic locators available

Scenario - 2
-------------
Even though if the elements are having attributes and the value of attributes are dynamically changing then how can we locate this element?
Answer: Xpath axes is best to use

Example is going to someone's house however, one needs to get to the Estate before getting to the house. Therefore, to the exact
house one needs to locate the estate through a specific landmark to avoid wrong turning in order to easily get to the estate where
the house is located.
The house is a Dynamically Changing Element.
The Landmark is an element with Absolute Value Static.

Solution
---------
Scenario 1: Locate an element whose values of attributes are static which is near to element not having attributes using Xpath.
Scenario 2: Located element is a Base Node or Current Node or Self Node or Context Node.
From the Base element Traverse or Move or Navigate to element through the DOM from top to bottom, bottom to top which is not having
any attributes or values of attributes changing.

XPath Axes
----------
To move or traverse from base element in DOM from top to bottom, bottom to top we need to use keywords which are called Xpath Axes.
In the process of moving, keywords or Xpath Axes are used to search for the multiple nodes in the XML document from the current node context.
Xpath axes or keywords should be used along with Xpath (directly jump to the element in the DOM).

Self (Optional)
Parent of a parent is called ancestor axis
Child of a child is called descendant axis
Brother and sister is called following-siblings axis
Nephew or niece are foreign siblings called proceeding siblings axis

E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By # 'by' is a module and inside it we have a class 'By'
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=opt)
driver.get("https://testautomationpractice.blogspot.com/") # driver.get helps to easily open url
driver.maximize_window() # this is use to expand the url page to fullscreen

# To avoid some exceptions implicit wait is used
driver.implicitly_wait(10)

# Lines of codes from 57 to 67 is Boiler Play Code is also known as Re-use-able Code
# For every automation script we use the same codes over and over again

# Any element that wants to be used is called Base Element/Nodes, Character Element/Nodes or Context Element/Nodes or Self Nodes for all
# Xpath will be used in this location

# Self (Optional) and using text method to get the text
# text_msg = driver.find_element(By.XPATH, "//td[text()='Animesh']").text
# print(text_msg)
'''
Output is 
Animesh
'''

# # Parent
# text_msg = driver.find_element(By.XPATH, "//td[text()='Animesh']/parent::tr").text
# print((text_msg))
'''
Output is 
Learn JS Animesh Javascript 300
'''

# Childs and using childs method and elements to return list due to multiple of children

# childs = driver.find_elements(By.XPATH, "//td[text()='Animesh']/parent::tr/child::td")
# print(len(childs))
'''
Output is 
4
'''

# Child
# child = driver.find_element(By.XPATH, "//td[text()='Animesh']/parent::tr/child::td")
# print(child.text)

'''
Output is
Learn JS
'''

# Childs with the for statement
# childs = driver.find_elements(By.XPATH, "//td[text()='Animesh']/parent::tr/child::td")
# for child in childs:
#     print(child.text)
'''
Output is
Learn JS
Animesh
Javascript
300
'''

# Ancestor
text_msg = driver.find_element(By.XPATH, "//td[text()='Animesh']/ancestor::tr").text
print((text_msg))
'''
Output is
Learn JS Animesh Javascript 300
'''

# Descendants
descendants = driver.find_elements(By.XPATH, "//td[text()='Animesh']/parent::tr/descendant::td")
print(len(descendants))
'''
Output is
4
'''

# Following
following = driver.find_elements(By.XPATH, "//td[text()='Animesh']/parent::tr/following::*")
print(len(following))
'''
Output is 
489
'''

# Preceding
preceding = driver.find_elements(By.XPATH, "//td[text()='Animesh']/parent::tr/preceding::*")
print(len(preceding))
'''
Output is 
300
'''



# Close the browser
driver.quit()