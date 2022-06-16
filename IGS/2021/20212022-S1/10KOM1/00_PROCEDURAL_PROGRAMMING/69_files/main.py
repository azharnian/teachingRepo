
with open('data.txt', 'r') as file:
	print(type(file))
	fruits = file.read()

print(type(fruits))
print(fruits)
our_fruits = fruits.split("\n")
print(our_fruits)