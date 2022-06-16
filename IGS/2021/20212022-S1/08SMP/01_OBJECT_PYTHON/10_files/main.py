fruits = []

with open('data.txt', 'r') as data: #read
	fruits = data.readlines()

# print(fruits) whitespace (newline/tab/space)
clean_fruits = []
for fruit in fruits:
	clean_fruit = fruit.strip()
	clean_fruits.append(clean_fruit)

print(clean_fruits)