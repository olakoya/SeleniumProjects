'''
Frames/Iframes
----------------
- A frame or iframe is an HTML Document inside another HTML Document.
- It is another source, advertisements, videos, interactive elements.
- It interacts with the elements in the currently focussed.
- To interacts it switches to that frame
- Iframe is called an inner frame ie a frame inside another frame

Commands to handle Frames
---------------------------
1. Driver variables required ie driver.switch_to.frame(using name or id attributes value) --> trying to switch to that frame
2. Webelements ie driver.switch_to.frame(webelement)
3. Index ie driver.switch_to.frame(index) => not always recommended [ele1,ele2]

driver.switch_to.frame(f1)
driver.switch_to.frame(f2)
driver.switch_to.frame(f3)
driver.find_element(ele) --> action

driver.switch_to.parent_frame() --> f2
driver.switch_to.parent_frame() --> f1

driver.switch_to.default_content()

- Frames are known ==> as forms or iframes
E.g
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

# Using a complete code ie element and frame combined for Frame 4
frame_4 = driver.find_element(By.XPATH, "//frame[@src='frame_4.html']")
driver.switch_to.frame(frame_4)
driver.find_element(By.XPATH, "//input[@name='mytext4']").send_keys("Ola")
'''
Output is
Web element displays and works as expected
'''

# Switching from Frame 4 to Frame 2
driver.switch_to.parent_frame()
frame_2 = driver.find_element(By.XPATH, "//frame[@src='frame_2.html']")
driver.switch_to.frame(frame_2)
driver.find_element(By.XPATH, "//input[@name='mytext2']").send_keys("Ola")
'''
Output is
Web elements display and work as expected for Frame 4 and Frame 2
'''


# Using plain find_element without frame
# driver.find_element(By.XPATH, "//input[@name='mytext4']").send_keys("Ola")
'''
Output is
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: 
{"method":"xpath","selector":"//input[@name='mytext4']"}
'''