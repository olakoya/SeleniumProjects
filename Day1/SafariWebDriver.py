from selenium import webdriver
opt=webdriver.SafariOptions()
# Initialize the Safari WebDriver
driver = webdriver.Safari(options=opt)

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

# Keep the browser open after the script finishes
input("Press Enter to close the browser...")

# Close the browser
driver.close()

'''
Output is
Title: Test Passed
'''