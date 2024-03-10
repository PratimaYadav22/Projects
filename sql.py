import sqlite3

connection = sqlite3.connect("employees.db")

#cursor for creating table, inserting values and retrieving results

cursor = connection.cursor()

table_information = """
CREATE TABLE EMPLOYEES (EMPLOYEE_ID INT, NAME VARCGAR(25), DEPT_NAME VARCHAR(25), DESIGNATION VARCHAR(10));
"""

cursor.execute(table_information)

cursor.execute('''Insert into EMPLOYEES values(1,'Pratima','Tech','Tech Lead')''')
cursor.execute('''Insert into EMPLOYEES values(2,'Gaurav','Tech','Manager')''')
cursor.execute('''Insert into EMPLOYEES values(3,'Shubham','Finance','Senior Analyst')''')
cursor.execute('''Insert into EMPLOYEES values(4,'Sara','Sales','Manager')''')
cursor.execute('''Insert into EMPLOYEES values(5,'Chinmay','Tech','SSE')''')
cursor.execute('''Insert into EMPLOYEES values(6,'John','Sales','Analyst')''')
cursor.execute('''Insert into EMPLOYEES values(7,'David','Tech','Data Analyst')''')
cursor.execute('''Insert into EMPLOYEES values(8,'Thomas','Sales','Representative')''')
cursor.execute('''Insert into EMPLOYEES values(9,'Jellena','Finance','Analyst')''')
cursor.execute('''Insert into EMPLOYEES values(10,'Andrew','Sales','Manager')''')


print("The inserted records are: ")

data = cursor.execute('''Select * from EMPLOYEES''')

for row in data:
    print(row)

connection.commit()
connection.close()