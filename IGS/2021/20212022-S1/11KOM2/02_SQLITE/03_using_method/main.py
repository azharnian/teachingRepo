import os

from settings import Settings
from employee import Employee

class App:

	def __init__(self):
		self.settings = Settings()

	def clear_screen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

	def get_all_emps(self):
		self.settings.cur.execute("""SELECT * FROM employees ORDER BY first""")
		return self.settings.cur.fetchall()

	# def insert_emp(self, emp):
	# 	self.settings.cur.execute("""INSERT INTO employees VALUES (:first, :last, :salary)""", {"first":emp.first, "last":emp.last, "salary":emp.salary})
	# 	self.settings.conn.commit()

	def insert_emp(self, emp):
		with self.settings.conn:
			self.settings.cur.execute("""INSERT INTO employees VALUES (:first, :last, :salary)""", {"first":emp.first, "last":emp.last, "salary":emp.salary})

	def find_emp_by_first_name(self, first):
		with self.settings.conn:
			self.settings.cur.execute("""SELECT * FROM employees WHERE first=:first""", {"first":first})
		return self.settings.cur.fetchone()

	def update_salary(self, emp, new_salary):
		with self.settings.conn:
			self.settings.cur.execute("""UPDATE employees SET salary=:salary WHERE first=:first """, {"salary":new_salary, "first":emp.first})

	def remove_emp(self, emp):
		with self.settings.conn:
			self.settings.cur.execute("""DELETE FROM employees WHERE first=:first AND last=:last""", {"first":emp.first, "last":emp.last})

	def mainloop(self):
		
		while True:
			self.clear_screen()

			print("""
			(1) SHOW ALL EMPLOYEES
			(2) ADD NEW EMPLOYEE
			(3) FIND EMPLOYEE BY NAME
			(4) UPDATE SALARY
			(5) REMOVE EMPLOYEE
			(Q) QUIT
				""")
			option = input("OPTION: ").lower()

			if option == "q":
				print("Thanks")
				break
			elif option == "1":
				self.clear_screen()
				emps = self.get_all_emps()
				print(emps)

			elif option == "2":
				self.clear_screen()
				first, last, salary = input().split()
				emp = Employee(first, last, salary)
				self.insert_emp(emp)
				print("done!")

			elif option == "3":
				self.clear_screen()
				first = input()
				res = self.find_emp_by_first_name(first)

				if res:
					print(res)
				else:
					print("nothing...")

			elif option == "4":
				self.clear_screen()
				first = input()
				res = self.find_emp_by_first_name(first)
				if res:
					new_salary = int(input())
					emp = Employee(res[0], res[1], res[2])
					self.update_salary(emp, new_salary)
					print("done!")
				else:
					print("nothing...")

			elif option == "5":
				pass

			input("Press Enter to Return")



if __name__ == '__main__':
	app = App()
	app.mainloop()
	app.settings.conn.close()