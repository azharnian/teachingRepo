

class Person:

	population = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.population += 1


print(Person.population)