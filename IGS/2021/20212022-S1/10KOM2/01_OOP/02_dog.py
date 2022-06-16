
class Dog:
	
	owner = "Anas"

	def __init__(self, name, age=0):
		self.name = name
		self.age = age

		# variable / lists / dicts dkk => atribute
		# function => method / ability

cutie = Dog(age=0, name="cutie")
print(cutie.name)

babe = Dog("babe", 0)
print(babe.name)

bim = Dog("bim")
print(bim.name, bim.age)

print(cutie.owner, babe.owner, bim.owner)
babe.owner = "Chalice"
print(cutie.owner, babe.owner, bim.owner)
Dog.owner = "Bhunaya"
print(cutie.owner, babe.owner, bim.owner)