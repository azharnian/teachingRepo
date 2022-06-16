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

print()
"""

stars = []

rows = 7
cols = 7

for row in range(rows):
	line = []
	for col in range(cols):
		print("*", end=" ")
		line.append("*")
	stars.append(line)
	print() # "\n"

print()

for row in stars:
	for star in row:
		print(star, end=" ")
	print()