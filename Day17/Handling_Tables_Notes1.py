'''
Handle Tables
---------------

Types of Tables
---------------
1. Web or HTML Table:
- This is an organised data in rows and columns

2. Operations on Table:
- This is counting rows and columns
- This reads data from table (i.e specific row and columns, and some condition)
- The row number and column number is not fixed ==> Variables

a. To use variables one needs Dynamic Xpath

b. Dynamic Xpath --> this is variables inside Xpath

c.//table[@name="BookTable"]//tr[7]/td[3] the rows tr[7] and data numbers td[3] are not fixed

Converting Integers to Strings
-------------------------------
tr["+str(r)+"]
td["+str(c)+"]

i Static Table
- This data is always fixed

ii Dynamic Table
- This data is always changing and it is not fixed

Table Tagname is Table only

Rows --> tr (table row)
Cols --> td (table data)
headers --> th (table headers)

cell(r,c)

range(2,11) --> 2 to 10

range(2,nosofrows+1) --> 2 to 6
ange(2,nosofcols+1)
'''
