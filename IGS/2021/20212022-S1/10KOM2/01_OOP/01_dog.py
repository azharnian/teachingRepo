
class Dog:
	
	def __init__(self, name): # fungsi construktor
		name = name
		self.age = 0
		self.isCute = True

	def roll_over(self):
		print(f"{name} rolled over...")

	def sleep(self):
		print(f'{self.name} : "zzzz"') # moly : "zzzz"

	def bark(self):
		print("Arrgghhh")


moly = Dog("moly")
print(moly.name)
print(moly.age)
print(moly.isCute)
moly.roll_over()

holy = Dog("holy")
print(holy.name)
holy.roll_over()
