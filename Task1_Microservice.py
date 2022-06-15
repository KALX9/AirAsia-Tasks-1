import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TES\SQLServer;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM products')

for i in cursor:
    print(i)

conn.commit()


