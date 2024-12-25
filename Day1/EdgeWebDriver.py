from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up Edge options
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the browser open after execution

# Create the Service object
service = Service(EdgeChromiumDriverManager().install())

# Initialize the WebDriver with Service and options
driver = webdriver.Edge(service=service, options=options)

# Open the application URL
driver.get("https://www.google.com/")
driver.maximize_window()

# Verify the page title
act_title = driver.title  # Actual title
exp_title = "Google"      # Expected title

# Check if the expected title matches the actual title
if act_title == exp_title:
    print("Title: Test Passed")
else:
    print("Title: Test Failed")

# Close the browser
driver.close()

'''
Output is 
Title: Test Passed
'''