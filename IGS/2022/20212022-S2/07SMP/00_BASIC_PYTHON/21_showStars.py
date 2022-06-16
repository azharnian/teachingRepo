
"""
stars = [
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"]
]
"""

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

"""

stars = []

rows = 20
cols = 20

for row in range(rows):
	line = []
	for col in range(cols):
		line.append("*")
	stars.append(line)



for row in stars:
	for star in row:
		print(star, end=" ")
	print()




