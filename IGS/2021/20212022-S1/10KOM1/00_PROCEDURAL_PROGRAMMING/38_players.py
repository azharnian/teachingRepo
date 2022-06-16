
players = ["charles", "martina", "michael"]

for player in players:
	print(player)

foods = ["pizza", "clementine", "pasta"]

for food in foods:
	print(food)

for number in range(2, 21, 2): #start, stop, step
	print(number, end=" ")
print()

#nested for
for i in range(1, 10):
	for j in range(1, 10):
		print("*", end=" ")
	print()