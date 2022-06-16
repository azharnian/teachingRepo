"""

rows = 5

* * * * *
* * * *
* * *
* *
*


rows = 6

* * * * * *
* * * * *
* * * *
* * *
* *
*

baris 1, bintang 6
baris 2, bintang 5

rows = n, 	->row = 1 star = n
			->row = 2 star = n-1

			->row = 0 star = n
			->row = 1 star = n - 1
			->row = 2 star = n - 2
			->row = a star = n - a
"""

rows = 6
for row in range(rows):
	for star in range(rows-row):
		print("*", end=" ")
	print()







	