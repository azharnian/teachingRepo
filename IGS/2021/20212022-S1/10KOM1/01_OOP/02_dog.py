
class Dog:

	owner = "Anas" # attribute di luar init ini
	
	def __init__(self, name): #fungsi konstruktor
		self.name = name
		self.age = 0 #month
		self.isCute = True

	def sit(self):
		print(f"{self.name} is sitting right now")


	def roll_over(self):
		print(f"{self.name} rolled over")

	def sleep(self):
		print(f'{self.name} : "zzzzz"')


		# variable, lists, dict dkk -> attribute
		# function -> method / ability

moly = Dog(name="Moly") 	# moly => object / instance
							# Dog() => class / template

moly.sit()
moly.roll_over()
moly.sleep()
