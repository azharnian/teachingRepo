
with open('data.txt', 'r') as file:
	fruits = file.readlines()

print(fruits)
clean_fruits = []
for fruit in fruits:
	clean_fruits.append(fruit.strip())
print(clean_fruits)
