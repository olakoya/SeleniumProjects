# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option("detach", True)
# opt.add_argument("--incognito")
# opt.add_experimental_option("excludeSwitches", ["enable-automation"])
# opt.add_argument("--lang=hi")
#
# driver = webdriver.Chrome(options=opt)
# driver.get("https://www.google.com/")
# driver.maximize_window()
#
# # Wait until the search box is clickable
# search_box = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.NAME, "q"))
# )
#
# # Now send keys
# search_box.send_keys("selenium" + Keys.RETURN)
#
# # driver.close()
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

# Start Chrome
driver = webdriver.Chrome(options=opt)
driver.get("https://www.google.com/")
driver.maximize_window()

# Locate search box with wait
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

# Type 'selenium' and wait for suggestions
search_box.send_keys("selenium")

# Wait for auto-suggestions to load
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li//span"))
)

# Get all suggestion elements
suggestions = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li//span")

# Print the number of suggestions and their text
print(f"Number of suggestions: {len(suggestions)}")
for suggestion in suggestions:
    print(suggestion.text)

# Optional: Close driver
driver.quit()
