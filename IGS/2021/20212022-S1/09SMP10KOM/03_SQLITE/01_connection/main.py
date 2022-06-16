import sqlite3

connection = sqlite3.connect("employee.db") # conn

cursor = connection.cursor() # c / cur

# cursor.execute("""
# 	CREATE TABLE IF NOT EXISTS employees (
# 	first TEXT,
# 	last TEXT,
# 	salary INTEGER
# 	)
# 	""")

# cursor.execute("INSERT INTO employees VALUES ('anisa', 'azhari', 8000000)") # CREATE

# cursor.execute("SELECT * FROM employees")

# emps = cursor.fetchall()
# print(emps)
# # for row in emps:
# # 	print(row)

# for first, last, salary in emps:
# 	print(first, last, salary)
# print()

cursor.execute("SELECT * FROM employees WHERE last='azhari'")

emp = cursor.fetchone()
print(emp)

connection.commit() # menyimpan perubahan kondisi database

connection.close()