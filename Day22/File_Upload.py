'''
File Upload
------------
Most of the web applications use sendkeys method --> send_keys() --> input
Or file upload window and to use it there's another model to use --> file_upload window

'''

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=en-uk")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
file1 = r"/Users/olakoya/Desktop/OlaKoyaCoveringLetter.pdf"
file2 = r"/Users/olakoya/Desktop/OlaKoyaCV.pdf"
driver.maximize_window()

# Uploading Single File
# driver.find_element(By.ID, "singleFileInput").send_keys(file1)
# driver.find_element(By.XPATH, "//button[text()='Upload Single File']").click()
#
# msg = driver.find_element(By.ID, "singleFileStatus").text
#
# if "OlaKoyaCoveringLetter.pdf" in msg:
#     print("Single file upload successful")
# else:
#     print("Single file upload unsuccessful")

'''
Output is
Single file upload successful
'''

# Uploading Multiple File
driver.find_element(By.ID, "multipleFilesInput").send_keys(f"{file1}\n{file2}")
driver.find_element(By.XPATH, "//button[text()='Upload Multiple Files']").click()

msg = driver.find_element(By.ID, "multipleFilesStatus").text
print(msg)

'''
Output is 
Multiple files selected:
OlaKoyaCoveringLetter.pdf, Size: 65663 bytes, Type: application/pdf
OlaKoyaCV.pdf, Size: 251920 bytes, Type: application/pdf
'''

if "OlaKoyaCoveringLetter.pdf" in msg and "OlaKoyaCV.pdf" in msg:
    print("Multiple files upload successful")
else:
    print("Multiple files upload unsuccessful")

'''
Output is
Multiple files selected:
OlaKoyaCoveringLetter.pdf, Size: 65663 bytes, Type: application/pdf
OlaKoyaCV.pdf, Size: 251920 bytes, Type: application/pdf
Multiple files upload successful
'''