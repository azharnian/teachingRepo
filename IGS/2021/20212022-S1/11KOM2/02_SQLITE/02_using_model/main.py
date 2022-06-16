import sqlite3

from employee import Employee

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS employees (first TEXT, last TEXT, salary INTEGER)")
conn.commit()

emp1 = Employee('anas', 'azhar', 3000)
emp2 = Employee('budi', 'sanusi', 5000)
emp3 = Employee('cindy', 'putri', 2500)

cur.execute("INSERT INTO employees VALUES (:first, :last, :salary)",{"first":emp3.first, "last":emp3.last, "salary":emp3.salary})
conn.commit()
conn.close()

"""
"INSERT INTO employees VALUES ('{}','{}','{}')".format(emp1.first, emp1.last, emp1.salary)
"INSERT INTO employees VALUES (?,?,?)",(emp2.first, emp2.last, emp2.salary)
"""