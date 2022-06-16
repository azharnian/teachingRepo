import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
				first TEXT, 
				last TEXT, 
				salary INTEGER)""")
connection.commit()

'''
cursor.execute("""INSERT INTO employees VALUES (
				'anisa',
				'azhari',
				5000) """)
connection.commit()


cursor.execute("""SELECT * FROM employees """)
emps = cursor.fetchall()
print(emps) #tuple in lists
'''

cursor.execute("""SELECT * FROM employees WHERE first='anas'""")
emp = cursor.fetchone()
print(emp) # tuple


connection.close()