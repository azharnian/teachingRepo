"""
*
* *
* * *
* * * *

row 1, col / star = 1
row 2, col / star = 2
row 3, col / star = 3

row n, col / star = n
python => 0

row 0, col 1
row n, col n + 1

"""

rows = 10

for row in range(rows):
	for star in range(row+1):
		print("*", end=" ")
	print()