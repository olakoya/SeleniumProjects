'''
Data Driven Testing
--------------------

Multiple sets of Data is required to test ---> Functionality (Test case) in the area of validation and this is known as ---> Data Driven Testing

Data Driven Testing are performed by Excel Files which is known as Database

To handle Excel Files we use Pandas or Openpyxl

Understanding Structure of Excel File
----------------------------------------
File --> load Workbook ---> to get Sheets ---> Rows and Columns ---> Cell(r,c)

Operations on Excel Files
-------------------------
This contains count of rows and columns
Reading data from all rows and columns, also specific column data
Write data into multiple cells

Read the Data from Cell
-------------------------
To read data, it contains sheet and cell of which will return cell i.e. data
= sheet.cell(r,c).value

How to write a Data from Cell?
-------------------------------
sheet.cell(r,c).value = data ---> save

when we are writing the data we should always close the file on which we are working

Data Driven Testing
------------------
Duplication of the code
Maintainability

Utility ==> a file contains reusable functions

To install packages
-------------------
pip install -r requirements.txt
pip install openpyxl

E.g
'''

import openpyxl
import os

file = r"/Users/olakoya/Desktop/Selenium/Day24/caldata.xlsx"

# try:
#     workbook = openpyxl.load_workbook(file)
#     print("Available sheets:", workbook.sheetnames)  # Print all sheet names
#
#     # Select the first available sheet instead of assuming "sheet1" exists
#     sheet_name = workbook.sheetnames[0]
#     sheet = workbook[sheet_name]
#     print(f"Using sheet: {sheet_name}")
#
# except Exception as e:
#     print("Error:", e)
'''
Output is
Available sheets: ['Sheet1']
Using sheet: Sheet1
'''

# Row and Colum Count
workbook = openpyxl.load_workbook(file)
sheet = workbook["Sheet1"]

print(sheet.max_row)
print(sheet.max_column)
'''
Output is
7
7
'''

# Reading a specific Cell Data
data = sheet.cell(4, 4).value
print(data)
'''
Output is
Compounded Annually
'''