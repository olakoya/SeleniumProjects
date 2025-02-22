'''
Data Driven Testing
--------------------

Multiple sets of Data is required to test ---> Functionality (Test case) in the area of validation and this is known as ---> Data Driven Testing

Data Driven Testing are performed by Excel Files which is known as Database

To handle Excel Files we use Pandas or Openpyxl

Understanding nStructure of Excel File
----------------------------------------
File --> Workbook ---> Sheets ---> Rows and Columns ---> Cell(r,c)

Operations on Excel Files
-------------------------
This contains count of rows and columns
Reading data from all rows and columns, also specific column data
Write data into multiple cells

Read the Data from Cell
-------------------------
To read data, it contains sheet and cell of which will return cell i.e. data = sheet.cell(r,c)

How to write a Data from Cell?
-------------------------------
sheet.cell(r,c) = data ---> save

when we are writing the data we should always close the file on which we are working

Data Driven Testing
------------------
Duplication of the code
Maintainability

Utility ==> a file contains reusable functions
'''