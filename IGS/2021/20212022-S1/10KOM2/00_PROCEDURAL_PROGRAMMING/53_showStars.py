"""
stars = [
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"]
]

for row in stars:
	for star in row:
		print(star, end=" ")
	print()

"""

stars = []

rows = 5
cols = 5

for row in range(rows):
	line = []
	for col in range(cols):
		print("*", end=" ")
		line.append("*")
	stars.append(line)
	print()

print()

for row in stars:
	for star in row:
		print(star, end=" ")
	print()
