'''
List1 = [Apple, Ball, Cat, Dog} ==> This a sorted list

list1.sort()

List of Comprehension
-----------------------
[expression of x sequence] for every element in the sequence apply some expression

E.g
'''

# List1 already sorted
# List1 = ["Apple", "Ball", "Cat", "Dog"]
# print(List1)
'''
Output is
['Apple', 'Ball', 'Cat', 'Dog']
'''
# sorted_list = List1.sort() # ["Apple", "Ball", "Cat", "Dog"]
# if sorted_list == List1:
#     print("Sorted List")
# else:
#     print("Unsorted List")
'''
Output is
Unsorted List
'''
# sorted_list = sorted(List1) # ["Apple", "Ball", "Cat", "Dog"]
# if sorted_list == List1:
#     print("Sorted List")
# else:
#     print("Unsorted List")
'''
Output is
Sorted List
'''

# List1 = ["Ball", "Dog", "Apple", "Cat"]
# sorted_list = sorted(List1) # ["Apple", "Ball", "Cat", "Dog"]
# if sorted_list == List1:
#     print("Sorted List")
# else:
#     print("Unsorted List")
'''
Output is
Unsorted List
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Unsorted Dropdown
# drop_down_element = driver.find_element(By.XPATH, "//select[@id= 'colors']")
# drop_down = Select(drop_down_element)
# options_text = [option.text for option in drop_down.options]
#
# print(options_text)
# '''
# Output is
# ['Red', 'Blue', 'Green', 'Yellow', 'Red', 'White', 'Green']
# '''
# if sorted(options_text) == options_text:
#     print("Sorted Dropdown")
# else:
#     print("Unsorted Dropdown")
'''
Output is 
['Red', 'Blue', 'Green', 'Yellow', 'Red', 'White', 'Green']
Unsorted Dropdown
'''

# Sorted Dropdown
drop_down_element = driver.find_element(By.XPATH, "//select[@id= 'animals']")
drop_down = Select(drop_down_element)
options_text = [option.text for option in drop_down.options]

print(options_text)
if sorted(options_text) == options_text:
    print("Sorted Dropdown")
else:
    print("Unsorted Dropdown")
'''
Output is
['Cat', 'Cheetah', 'Deer', 'Dog', 'Elephant', 'Fox', 'Giraffe', 'Lion', 'Rabbit', 'Zebra']
Sorted Dropdown
'''