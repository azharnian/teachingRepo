#Object Oriented Prgramming
#Variable = Attribute
#Function = Methods
class Dog:

	def __init__(self, name, age):
		"""
		initialize / awal object akan diciptakan 
		"""
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name} is sitting right now.")

	def roll_over(self):
		print(f"{self.name} rolled over.")


my_dog = Dog(name="Hocky", age=10)
print(f"My dog's name is {my_dog.name}")
print(f"It is {my_dog.age} months")
my_dog.sit()
my_dog.roll_over()

my_2nd_dog = Dog(name="Heli", age=5)
print(f"My 2nd dog's name is {my_2nd_dog.name}")
print(f"It is {my_2nd_dog.age} months")
my_2nd_dog.sit()
my_2nd_dog.roll_over()