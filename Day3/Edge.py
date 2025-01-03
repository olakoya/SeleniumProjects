from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Setting up Chrome options
options = webdriver.EdgeOptions()
options.add_experimental_option("detach" , True)
# Creating the Service object
# service = Service(ChromeDriverManager().install())

# Initializing the WebDriver with Service and options
driver = webdriver.Edge(options=options)

# Perform task
driver.get("https://www.facebook.com/")
print("Navigated to the website")
driver.maximize_window()

# Using nos 4 from the above combined css selectors notes
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys(("Ola"))