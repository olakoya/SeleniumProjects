# Boiler Codes First below i.e. reused codes importing libraries from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# set up chrome option
# class method is chromeoptions and object reference variable is options

# set up chrome options
options = webdriver.ChromeOptions()
# keeps the browser open after execution
options.add_experimental_option("detach", True) # specifying method and passing an arguement

# Create the Service object with ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Initialise the Webdriver with the options
driver = webdriver.Chrome(service=service, options=options)# webdriver is a module and consists of a class 'chrome'
# browser specific option is chromeoptions
# options is a parameter while opt is a value as taught in the class but not using opt due to my mac operating system
# option reference variable is driver

# With the help of driver open an application url
driver.get("https://www.google.com/")
driver.maximize_window()

# verify the page title
act_title = driver.title # actual title
exp_title = "Google" # expected title

# checking with a condition statement if expected title is accurate
if act_title == exp_title:
    print("Title: Test Passed")
else:
    print("Title: Test Failed")

# close the browser
driver.close()

'''
Output is 
Title: Test Passed
'''

'''
Output after editing line 28 with a wrong Google spelling 'Googleing' is 
Title: Test Failed
'''
'''
Output when commenting line 36 is that chrome page didn't close automatically after opening
Title: Test Passed
'''
