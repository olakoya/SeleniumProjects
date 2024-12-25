from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox options
options = webdriver.FirefoxOptions()
# options.add_experimental_option("detach", True)  # Keeps the browser open after execution

# Create the Service object
service = Service(GeckoDriverManager().install())

# Initialize the WebDriver with Service and options
driver = webdriver.Firefox(service=service, options=options)

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

# Keep the browser open after the script finishes (useful for debugging)
# input("Press Enter to close the browser...")

# Close the browser
driver.close()

'''
Output after commenting line 7 is 
Title: Test Passed
'''