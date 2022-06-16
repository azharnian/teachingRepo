

class Person:

	population = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.population += 1


	def display(self):
		print(self.name, 'is', self.age, "years old")

	def get_population_number(self):
		print(self.population)

	@staticmethod
	def isAdult(age):
		return age >= 18

	@classmethod
	def get_population(self):
		return Person.population

print(Person.isAdult(30))
print(Person.get_population())

"""
bryan = Person("Bryan", 17)

bryan.display()
bryan.get_population_number()

sallini = Person("Sallini", 18)
sallini.display()
sallini.get_population_number()
"""

