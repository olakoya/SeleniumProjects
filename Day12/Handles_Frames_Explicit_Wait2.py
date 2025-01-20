from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

my_wait = WebDriverWait(driver,10) # Declaration
my_wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//frame[@src='frame_4.html']")))
driver.find_element(By.XPATH, "//input[@name='mytext4']").send_keys("Ola")
'''
Output is
Web element displays and works as expected
'''