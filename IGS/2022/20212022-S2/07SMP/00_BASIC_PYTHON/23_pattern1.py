"""
rows = 5

* * * * *
* * * *
* * *
* *
*

baris 0, bintang 5
baris 1, bintang 4
baris 2, bintang 3
baris 3, bintang 2
baris 4, bintang 1

rows = n

baris 0, bintang n - 0
baris 1, bintang n - 1
baris 2, bintang n - 2
baris a, bintang n - a

row = 0, rows - row

"""

rows = 6

for row in range(rows):
	for star in range(rows-row):
		print("*", end=" ")
	print()
