# import math

# print(math.sqrt(4))

class Person:

	population = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.population += 1

	def display(self):
		print(f" {self.name} is {self.age} years old.")

	#using instance object
	def get_population(self):
		print(self.population)

	@classmethod
	def get_population_class(self):
		print(Person.population)

	@staticmethod
	def isAdult(age):
		return age >= 18


bryan = Person("Bryan", 30)
bryan.display()

print(bryan.isAdult(bryan.age))
# charlos = Person("Charlos", 20)
# charlos.display()

# print(Person.population)
Person.get_population_class()

print(Person.isAdult(20))

