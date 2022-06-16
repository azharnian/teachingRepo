"""

*
* *
* * *
* * * *

baris 1 , bintang / kolom 1
baris 2, bintang 2
baris 3, bintang 3, row = n -> star = n = row

baris 0 , bintang 1, row = n -> star = n+1 = row+1
"""

rows = 10

# range -> rage(start, stop, step)

for row in range(rows): # range(5) -> range(0, 5, 1), range(1, 5) -> range(1, 5, 1), range(1, 11, 2)
	for star in range(row+1):
		print("*", end=" ")

	print()