'''
Mouse Operations
------------------
There is a specific method that is ActionChains Class which is a ---> methods

Mouse Operations are:
---------------------
     mouse hover() --> move_to_element
     double click() --> double_click
     right click operations()
     drag and drop() --> drag_and_drop
     slider() --> drag_and_drop_offset
     right click() --> context_click()
     scrolling() --> scroll_to_element
     .perform()

NB: Scroll on webpage is from browser and not from webpage
'''
# Boiler Codes are reused to begin the code lines i.e. importing libraries from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=en-uk")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

act = ActionChains(driver) # act is object reference variable

# 1. Scrolling the Page to Element on WebPage
copy_text = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
act.scroll_to_element(copy_text).perform()

# 2. Mouse Hover ---> move_to_element
ele = driver.find_element(By.CLASS_NAME, "dropbtn")
act.move_to_element(ele).perform()

# 3. Double Click Method --> double_click()
act.double_click(copy_text).perform()

# 4. Drag and Drop --> drag_and_drop()
src = driver.find_element(By.ID, "draggable")
trg = driver.find_element(By.ID, "droppable")
act.drag_and_drop(src,trg).perform()

# 5. Slider
src = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print(src.location)
act.drag_and_drop_by_offset(src,-20,5).perform()
print(src.location)

'''
Output is for 30, 0
{'x': 935, 'y': 1975}
{'x': 935, 'y': 1975}


Output after adding -30, .perform() to line 55
{'x': 935, 'y': 1975}
{'x': 905, 'y': 1975}

-20, 5
{'x': 935, 'y': 1975}
{'x': 914, 'y': 1975}
'''