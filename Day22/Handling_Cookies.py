# Boiler Codes are reused to begin the code lines i.e. importing libraries from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach" , True)
opt.add_argument("--incognito")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--lang=hi")

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.get("https://www.amazon.com/")
# driver.get("https://www.facebook.com/")
# driver.get("https://www.ebay.com/")
# driver.get("https://www.gumtree.com/")
driver.get("https://dengro.com")
driver.maximize_window()


# Get all Cookies
cookies = driver.get_cookies()
# print(len(cookies))
# print(cookies)

'''
Output for https://testautomationpractice.blogspot.com/ is
0

Output for https://www.amazon.com/ is
6
[{'domain': '.amazon.com', 'expiry': 1770983472, 'httpOnly': False, 'name': 'session-id-time', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '2082787201l'}, 
{'domain': '.amazon.com', 'expiry': 1770983472, 'httpOnly': False, 'name': 'session-id', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '131-4473754-8249062'}, 
{'domain': 'www.amazon.com', 'expiry': 1769687472, 'httpOnly': False, 'name': 'csm-hit', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tb:s-Y8GWZ9DFBWW0TDN0Q47Z|1739447472022&t:1739447472135&adb:adblk_no'}, 
{'domain': '.amazon.com', 'expiry': 1770983472, 'httpOnly': True, 'name': 'sp-cdn', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"L5Z9:GB"'}, 
{'domain': '.amazon.com', 'expiry': 1770983472, 'httpOnly': False, 'name': 'i18n-prefs', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'USD'}, 
{'domain': '.amazon.com', 'httpOnly': False, 'name': 'skin', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'noskin'}]

Output for https://www.facebook.com/ is
0

Output for https://www.ebay.com/ is
8

https://www.gumtree.com/
12

("https://dengro.com")
5
[{'domain': '.dengro.com', 'httpOnly': False, 'name': '__hssrc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, 
{'domain': '.dengro.com', 'expiry': 1754999332, 'httpOnly': False, 'name': 'hubspotutk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '26703ac42e9aee1aaa4608ad06fdaea0'}, 
{'domain': '.dengro.com', 'expiry': 1739449132, 'httpOnly': False, 'name': '__hssc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '182600377.1.1739447332566'}, 
{'domain': '.dengro.com', 'expiry': 1754999332, 'httpOnly': False, 'name': '__hstc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '182600377.26703ac42e9aee1aaa4608ad06fdaea0.1739447332566.1739447332566.1739447332566.1'}, 
{'domain': 'dengro.com', 'expiry': 1770983331, 'httpOnly': False, 'name': 'cookieyes-consent', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': 'consentid:ZXhsZmVneEZ6Z0kxZFhicndZRk1VZDFJcmVxV01FS08,consent:,action:,necessary:,functional:,analytics:,performance:,advertisement:'}]

'''

# To interact with the cookies
# for c in cookies:
#     print(c)
#     print(c.get("name"), ":", c.get("value"))

'''
Output for Ebay is
5
[{'domain': '.ebay.com', 'expiry': 1739455146, 'httpOnly': False, 'name': 'ak_bmsc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '785C372BE632D29A2B899C577532A3C6~000000000000000000000000000000~YAAQzKMQAkWR77yUAQAAj04t/xo5rKJKUQPbGYn9QMVjAof1+yRPPbuU7HkgngZgK2+Pjy86G21jte/0vosqlHNMZ0ataFipB4ZHxzCN3dQ4YxO+np2QX1OL7R0HvRHkv/alPr8jqTKxC4yo3/zyyfY7gnvZFAWiGXECzEp2Toes/8049WcdZHIuXlHO8wwPT+T0YoyGCbKOcJB4F2B7pRuiHMHssB2vrkn2vqC/TGnlWftDy2wHsx4B0c5wpTPp+1nrLTurEglT16LJekdVvwx0xe9P/HJ+oYtgaAhElCs3uIL/Rl2DytOq0IT+wyaxlcqghqBJ9IFaofsBgNlak0KoP6qklcTCNCWpHBwBae5ZLMMfVKAAQV2b8V+V8VqJywtIogP5q9s='}, {'domain': '.ebay.com', 'httpOnly': False, 'name': 'ebay', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%5Esbf%3D%23100000%5E'}, {'domain': '.ebay.com', 'expiry': 1774007946, 'httpOnly': True, 'name': 'nonsession', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'BAQAAAZRXz2gmAAaAADMAB2mPEgpNTDExMFNFAMoAIGtwRYpmZjJkNGUxYzE5NDBhNzI4NmNhMGNjYjhmZmZmYzUxYgDLAAFnreWSMXRP7E77/G4esA4CdEqxktsl9t27'}, {'domain': '.ebay.com', 'httpOnly': True, 'name': 's', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'CgAD4ACBnrzAKZmYyZDRlMWMxOTQwYTcyODZjYTBjY2I4ZmZmZmM1MWK0g7b+'}, {'domain': '.ebay.com', 'expiry': 1774007946, 'httpOnly': False, 'name': 'dp1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'bbl/GB6b70458a^'}]
{'domain': '.ebay.com', 'expiry': 1739455146, 'httpOnly': False, 'name': 'ak_bmsc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '785C372BE632D29A2B899C577532A3C6~000000000000000000000000000000~YAAQzKMQAkWR77yUAQAAj04t/xo5rKJKUQPbGYn9QMVjAof1+yRPPbuU7HkgngZgK2+Pjy86G21jte/0vosqlHNMZ0ataFipB4ZHxzCN3dQ4YxO+np2QX1OL7R0HvRHkv/alPr8jqTKxC4yo3/zyyfY7gnvZFAWiGXECzEp2Toes/8049WcdZHIuXlHO8wwPT+T0YoyGCbKOcJB4F2B7pRuiHMHssB2vrkn2vqC/TGnlWftDy2wHsx4B0c5wpTPp+1nrLTurEglT16LJekdVvwx0xe9P/HJ+oYtgaAhElCs3uIL/Rl2DytOq0IT+wyaxlcqghqBJ9IFaofsBgNlak0KoP6qklcTCNCWpHBwBae5ZLMMfVKAAQV2b8V+V8VqJywtIogP5q9s='}
{'domain': '.ebay.com', 'httpOnly': False, 'name': 'ebay', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%5Esbf%3D%23100000%5E'}
{'domain': '.ebay.com', 'expiry': 1774007946, 'httpOnly': True, 'name': 'nonsession', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'BAQAAAZRXz2gmAAaAADMAB2mPEgpNTDExMFNFAMoAIGtwRYpmZjJkNGUxYzE5NDBhNzI4NmNhMGNjYjhmZmZmYzUxYgDLAAFnreWSMXRP7E77/G4esA4CdEqxktsl9t27'}
{'domain': '.ebay.com', 'httpOnly': True, 'name': 's', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'CgAD4ACBnrzAKZmYyZDRlMWMxOTQwYTcyODZjYTBjY2I4ZmZmZmM1MWK0g7b+'}
{'domain': '.ebay.com', 'expiry': 1774007946, 'httpOnly': False, 'name': 'dp1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'bbl/GB6b70458a^'}

Output after adding line 60
12
[{'domain': '.ebay.com', 'expiry': 1739455355, 'httpOnly': False, 'name': 'bm_sv', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'C1745A98BBE6D0DF2CED289878AA6B8C~YAAQ1KMQAie0uryUAQAAHXww/xqTlVoZmPfIz1EmLVL5Bmo+qt5xnxn+/p6YGhsNF0WPww99xizLB+YoDeQJTSSgNICrDeFs1tkYl+okQJyBjUxjfOWYzqrWrg8QR218D2a9bzcpf8vk0+hgtYnaxOw0PIfD8lHwjgQBgQuKOiL/QID5HtalDWuT8X4RagUmTHfrYe0MNgzA27ihOB1klekUnKh3a9gaeXkJOF9HpxM/kyBl9VM9oyc4I/4zEA==~1'}, {'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmb', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1739448155'}, {'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmd', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1739448155'}, {'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzma', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '3ace11a3-9db0-4388-82cb-01bd30d79d68'}, {'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '7f60002ad43e6d-f624-4f7e-9d34-d88a981431d517394481550370-2176737b5ca9058d10'}, {'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzme', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '6811'}, {'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '819081026093'}, {'domain': '.ebay.com', 'expiry': 1774008155, 'httpOnly': True, 'name': 'nonsession', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'BAQAAAZRXz2gmAAaAADMAB2mPEttNTDExMFNFAMoAIGtwRltmZjMwNzg4YjE5NDBhNjI1MzUyMWZkNTlmZmZmZmFlNADLAAFnreZjMYMg6rKoFmFPWfySKfSrSsX4VHIA'}, {'domain': '.ebay.com', 'expiry': 1739455354, 'httpOnly': False, 'name': 'ak_bmsc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '267A91E5F94CE8D1DBCB362BDEC95C10~000000000000000000000000000000~YAAQ1KMQAtCyuryUAQAAHXkw/xr6bpiqqm2zkgfEUYDbMvOuqvfsy5g7FenEWvcXRwxFBPZ1ATpDf1ggSYYXqVL4sTzUN7O3rFAGM5mYQOG86pPhf9KLfr5N9EmThti59mX5OLY9q/s/T6pdwkYL7qkX7j58gXrKMJGrpwZ3vy4XsGwgm5iA8JUDcfISEk2gTL7kHfP54p+R0gbclwat4UNSMD5puBJLLdza9SYabscAdgkeNOd1PPykNR4haV27MI79Kv1G9qADWkrbf32hHYXrWzZ0ruleZwALAGDndZHJKL+glV/iTbrYAIb/xgtqiZxEw0lDYTAIfj3fOiLZiSoYMKRo0AD6LWXH3TYJv/q5tWoOOe60SHEsohLdPOg9t/+n+mJ7B34='}, {'domain': '.ebay.com', 'httpOnly': False, 'name': 'ebay', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '%5Esbf%3D%23000000%5E'}, {'domain': '.ebay.com', 'expiry': 1774008155, 'httpOnly': False, 'name': 'dp1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'bbl/GB6b70465b^'}, {'domain': '.ebay.com', 'httpOnly': True, 'name': 's', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'CgAD4ACBnrzDaZmYzMDc4OGIxOTQwYTYyNTM1MjFmZDU5ZmZmZmZhZTQT4DVl'}]
{'domain': '.ebay.com', 'expiry': 1739455355, 'httpOnly': False, 'name': 'bm_sv', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'C1745A98BBE6D0DF2CED289878AA6B8C~YAAQ1KMQAie0uryUAQAAHXww/xqTlVoZmPfIz1EmLVL5Bmo+qt5xnxn+/p6YGhsNF0WPww99xizLB+YoDeQJTSSgNICrDeFs1tkYl+okQJyBjUxjfOWYzqrWrg8QR218D2a9bzcpf8vk0+hgtYnaxOw0PIfD8lHwjgQBgQuKOiL/QID5HtalDWuT8X4RagUmTHfrYe0MNgzA27ihOB1klekUnKh3a9gaeXkJOF9HpxM/kyBl9VM9oyc4I/4zEA==~1'}
bm_sv : C1745A98BBE6D0DF2CED289878AA6B8C~YAAQ1KMQAie0uryUAQAAHXww/xqTlVoZmPfIz1EmLVL5Bmo+qt5xnxn+/p6YGhsNF0WPww99xizLB+YoDeQJTSSgNICrDeFs1tkYl+okQJyBjUxjfOWYzqrWrg8QR218D2a9bzcpf8vk0+hgtYnaxOw0PIfD8lHwjgQBgQuKOiL/QID5HtalDWuT8X4RagUmTHfrYe0MNgzA27ihOB1klekUnKh3a9gaeXkJOF9HpxM/kyBl9VM9oyc4I/4zEA==~1
{'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmb', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1739448155'}
__uzmb : 1739448155
{'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmd', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1739448155'}
__uzmd : 1739448155
{'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzma', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '3ace11a3-9db0-4388-82cb-01bd30d79d68'}
__uzma : 3ace11a3-9db0-4388-82cb-01bd30d79d68
{'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '7f60002ad43e6d-f624-4f7e-9d34-d88a981431d517394481550370-2176737b5ca9058d10'}
__uzmf : 7f60002ad43e6d-f624-4f7e-9d34-d88a981431d517394481550370-2176737b5ca9058d10
{'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzme', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '6811'}
__uzme : 6811
{'domain': '.ebay.com', 'expiry': 1755000155, 'httpOnly': False, 'name': '__uzmc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '819081026093'}
__uzmc : 819081026093
{'domain': '.ebay.com', 'expiry': 1774008155, 'httpOnly': True, 'name': 'nonsession', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'BAQAAAZRXz2gmAAaAADMAB2mPEttNTDExMFNFAMoAIGtwRltmZjMwNzg4YjE5NDBhNjI1MzUyMWZkNTlmZmZmZmFlNADLAAFnreZjMYMg6rKoFmFPWfySKfSrSsX4VHIA'}
nonsession : BAQAAAZRXz2gmAAaAADMAB2mPEttNTDExMFNFAMoAIGtwRltmZjMwNzg4YjE5NDBhNjI1MzUyMWZkNTlmZmZmZmFlNADLAAFnreZjMYMg6rKoFmFPWfySKfSrSsX4VHIA
{'domain': '.ebay.com', 'expiry': 1739455354, 'httpOnly': False, 'name': 'ak_bmsc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '267A91E5F94CE8D1DBCB362BDEC95C10~000000000000000000000000000000~YAAQ1KMQAtCyuryUAQAAHXkw/xr6bpiqqm2zkgfEUYDbMvOuqvfsy5g7FenEWvcXRwxFBPZ1ATpDf1ggSYYXqVL4sTzUN7O3rFAGM5mYQOG86pPhf9KLfr5N9EmThti59mX5OLY9q/s/T6pdwkYL7qkX7j58gXrKMJGrpwZ3vy4XsGwgm5iA8JUDcfISEk2gTL7kHfP54p+R0gbclwat4UNSMD5puBJLLdza9SYabscAdgkeNOd1PPykNR4haV27MI79Kv1G9qADWkrbf32hHYXrWzZ0ruleZwALAGDndZHJKL+glV/iTbrYAIb/xgtqiZxEw0lDYTAIfj3fOiLZiSoYMKRo0AD6LWXH3TYJv/q5tWoOOe60SHEsohLdPOg9t/+n+mJ7B34='}
ak_bmsc : 267A91E5F94CE8D1DBCB362BDEC95C10~000000000000000000000000000000~YAAQ1KMQAtCyuryUAQAAHXkw/xr6bpiqqm2zkgfEUYDbMvOuqvfsy5g7FenEWvcXRwxFBPZ1ATpDf1ggSYYXqVL4sTzUN7O3rFAGM5mYQOG86pPhf9KLfr5N9EmThti59mX5OLY9q/s/T6pdwkYL7qkX7j58gXrKMJGrpwZ3vy4XsGwgm5iA8JUDcfISEk2gTL7kHfP54p+R0gbclwat4UNSMD5puBJLLdza9SYabscAdgkeNOd1PPykNR4haV27MI79Kv1G9qADWkrbf32hHYXrWzZ0ruleZwALAGDndZHJKL+glV/iTbrYAIb/xgtqiZxEw0lDYTAIfj3fOiLZiSoYMKRo0AD6LWXH3TYJv/q5tWoOOe60SHEsohLdPOg9t/+n+mJ7B34=
{'domain': '.ebay.com', 'httpOnly': False, 'name': 'ebay', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '%5Esbf%3D%23000000%5E'}
ebay : %5Esbf%3D%23000000%5E
{'domain': '.ebay.com', 'expiry': 1774008155, 'httpOnly': False, 'name': 'dp1', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'bbl/GB6b70465b^'}
dp1 : bbl/GB6b70465b^
{'domain': '.ebay.com', 'httpOnly': True, 'name': 's', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'CgAD4ACBnrzDaZmYzMDc4OGIxOTQwYTYyNTM1MjFmZDU5ZmZmZmZhZTQT4DVl'}
s : CgAD4ACBnrzDaZmYzMDc4OGIxOTQwYTYyNTM1MjFmZDU5ZmZmZmZhZTQT4DVl


Output for Facebook is
0
[]
'''

# To add a Cookie
driver.add_cookie({"name": "UserID", "value": "abc123456"})
driver.add_cookie({"name": "AuthToken", "value": "token987654"})
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

print(driver.get_cookie("AuthToken"))

'''
Output is
1

Output after adding line 110
2
'''

# To delete Cookie
# driver.delete_all_cookies()

'''
Output after deleting all cookies on Facebook
2

For Dengro
7

After Adding Dengro
7
[{'domain': 'dengro.com', 'httpOnly': False, 'name': 'UserID', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'abc123456'}
, {'domain': 'dengro.com', 'expiry': 1771183709, 'httpOnly': False, 'name': 'cookieyes-consent', 'path': '/', 'sameSite': 'Strict', 
'secure': True, 'value': 'consentid:RjVjQVd2OWhaOVJmZmJmZmQ5ZHdKNkY5eDcyVmxwWDU,consent:,action:,necessary:,functional:,analytics:,
performance:,advertisement:'}, {'domain': '.dengro.com', 'expiry': 1739649509, 'httpOnly': False, 'name': '__hssc', 'path': '/', 
'sameSite': 'Lax', 'secure': False, 'value': '182600377.1.1739647709539'}, {'domain': '.dengro.com', 'httpOnly': False, 'name': 
'__hssrc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': 'dengro.com', 'httpOnly': False, 'name': 
'AuthToken', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'token987654'}, {'domain': '.dengro.com', 'expiry': 1755199709
, 'httpOnly': False, 'name': 'hubspotutk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '6af45e6c0f9382bdd4f70027594ad4
57'}, {'domain': '.dengro.com', 'expiry': 1755199709, 'httpOnly': False, 'name': '__hstc', 'path': '/', 'sameSite': 'Lax', 'secure':
 False, 'value': '182600377.6af45e6c0f9382bdd4f70027594ad457.1739647709539.1739647709539.1739647709539.1'}]
 
 {'domain': 'dengro.com', 'httpOnly': False, 'name': 'AuthToken', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'token987654'}
'''

# Deleting Cookie Method
driver.delete_cookie("AuthToken")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()

'''
Output is 
7
[{'domain': 'dengro.com', 'httpOnly': False, 'name': 'UserID', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'abc123456'}
, {'domain': 'dengro.com', 'expiry': 1771184542, 'httpOnly': False, 'name': 'cookieyes-consent', 'path': '/', 'sameSite': 'Strict', 
'secure': True, 'value': 'consentid:UDAya1VMOENCU0NBVXJiN01ZYU1IeU94dGFneU5HRUE,consent:,action:,necessary:,functional:,analytics:,
performance:,advertisement:'}, {'domain': '.dengro.com', 'expiry': 1739650344, 'httpOnly': False, 'name': '__hssc', 'path': '/', 
'sameSite': 'Lax', 'secure': False, 'value': '182600377.1.1739648544778'}, {'domain': '.dengro.com', 'httpOnly': False, 'name': '__
hssrc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': 'dengro.com', 'httpOnly': False, 'name': 'AuthToken'
, 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'token987654'}, {'domain': '.dengro.com', 'expiry': 1755200544, 'httpOnly
': False, 'name': 'hubspotutk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b18a414e3fb4777af856a6acc275c41e'}, {'domain
': '.dengro.com', 'expiry': 1755200544, 'httpOnly': False, 'name': '__hstc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value':
 '182600377.b18a414e3fb4777af856a6acc275c41e.1739648544778.1739648544778.1739648544778.1'}]
{'domain': 'dengro.com', 'httpOnly': False, 'name': 'AuthToken', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'token987654'}

Output after subtracting one cookie after execution
6
[{'domain': 'dengro.com', 'httpOnly': False, 'name': 'UserID', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'abc123456'}, 
{'domain': 'dengro.com', 'expiry': 1771184542, 'httpOnly': False, 'name': 'cookieyes-consent', 'path': '/', 'sameSite': 'Strict', 
'secure': True, 'value': 'consentid:UDAya1VMOENCU0NBVXJiN01ZYU1IeU94dGFneU5HRUE,consent:,action:,necessary:,functional:,analytics:,
performance:,advertisement:'}, {'domain': '.dengro.com', 'expiry': 1739650344, 'httpOnly': False, 'name': '__hssc', 'path': '/', 
'sameSite': 'Lax', 'secure': False, 'value': '182600377.1.1739648544778'}, {'domain': '.dengro.com', 'httpOnly': False, 'name': 
'__hssrc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': '.dengro.com', 'expiry': 1755200544, 'httpOnly
': False, 'name': 'hubspotutk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'b18a414e3fb4777af856a6acc275c41e'}, 
{'domain': '.dengro.com', 'expiry': 1755200544, 'httpOnly': False, 'name': '__hstc', 'path': '/', 'sameSite': 'Lax', 'secure': 
False, 'value': '182600377.b18a414e3fb4777af856a6acc275c41e.1739648544778.1739648544778.1739648544778.1'}]

'''
driver.close()