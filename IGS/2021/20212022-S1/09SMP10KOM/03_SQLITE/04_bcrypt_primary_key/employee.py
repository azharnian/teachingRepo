
class Employee:

	counter = 1

	def __init__(self, username, first, last, salary):
		self.id = Employee.counter
		self.username = username
		self.password = None
		self.first = first
		self.last = last
		self.salary = salary

		Employee.counter += 1