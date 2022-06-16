"""

*
**
***
****
*****

"""

# stars = [
# 	["*"],
# 	["*", "*"],
# 	["*", "*", "*"]
# ]

# banyak bintang pada kolom sesuai dengan baris ke-n

rows = 5 #0, 1, 2, 3, 4

for row in range(rows): # range(5) -> range(0, 5, 1), range(1, 10) -> range(1, 10, 1)
	for star in range(row+1): # range(start, stop, step) -> range(6, -1, -1)
		print("*", end="")
	print()


"""
rows = 6
******
*****
****
***
**
*

"""
print()
rows = 7

for row in range(rows):
	for star in range(rows-row):
		print("*", end="")
	print()


