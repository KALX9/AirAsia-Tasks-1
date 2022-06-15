# AirAsia-Tasks-1

Write a microservice that interacts with database(any) in Python/Go.

## Step 1: Create a Database and Table ( Table created seperately & linked to application)

For demo purpose, below values are used.
----------------------
Server name is: TES\SQLServer
Database name is: test_database
Table name is: products

The ‘products’ table contains the following data:
product_id	product_name	price
1	          Laptop	          1100
2	          Printer	          200
3	          Keyboard	          80
4	          Monitor	          450
5	          Tablet	          300

## Step 2: Connect Python to SQL Server
Used "pyodbc" which is an open source Python module that makes accessing ODBC databases simple.

Below is the code to connect Python to SQL Server,

import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TES\SQLServer;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM products')

for i in cursor:
    print(i)
    
## Run the code in Python (adjusted to your server, database and table information), and you’ll see the following result:

(1, 'Laptop', 1100)
(2, 'Printer', 200)
(3, 'Keyboard', 80)
(4, 'Monitor', 450)
(5, 'Tablet', 300)

## Step 3: Update the Records in SQL Server using Python
After you connected Python and SQL Server, you’ll be able to update the records in SQL Server using Python.
Here is the template that you may apply in Python to update the records:

import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
                UPDATE products
                SET price = 350
                WHERE product_id = 5
                ''')

conn.commit()

## ------------------------------------------------------------------




