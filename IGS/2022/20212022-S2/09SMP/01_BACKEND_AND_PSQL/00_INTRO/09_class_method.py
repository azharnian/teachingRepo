

class Person:

	population = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.population += 1

	@classmethod
	def get_population(self):
		print(Person.population)



anas = Person("Anas", 27)
# print(Person.population)
# print(anas.population)

Person.get_population()
anas.get_population()
