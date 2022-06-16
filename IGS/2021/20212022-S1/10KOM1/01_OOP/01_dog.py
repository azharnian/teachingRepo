
class Dog:

	owner = "Anas" # attribute di luar init ini
	
	def __init__(self, name): #fungsi konstruktor
		self.name = name
		self.age = 0 #month
		self.isCute = True

moly = Dog(name="Moly") 	# moly => object / instance
							# Dog() => class / template
# print(moly)
print(moly.name)
print(moly.age)
print(moly.isCute)

holy = Dog(name="Holy")

print(holy.name)
print(holy.age)
print(holy.isCute)

Dog.owner = "Budi"
print(holy.owner)
print(moly.owner)

Dog.name = "Doly"
print(holy.name)