
#table in sql -> model object class
class Employee:

	def __init__(self, first, last, salary=0):
		self.first = first
		self.last = last
		self.salary = salary