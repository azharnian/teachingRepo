
class Dog:
	
	name = "Moly"
	age = 0 #month
	isCute = True

moly = Dog() 	# moly => object / instance
				# Dog() => class / template
# print(moly)
print(moly.name)
print(moly.age)
print(moly.isCute)

holy = Dog()

print(holy.name)
print(holy.age)
print(holy.isCute)

Dog.age += 1
print(holy.age) # 0/1 ?