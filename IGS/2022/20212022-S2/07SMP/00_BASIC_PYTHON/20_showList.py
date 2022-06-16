

#alist = [1, 2, 3, 4, 5]

lists = [
	[1, 2, 3, 4, 5],
	[6, 7, 8, 9, 10],
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20]
]


"""
for item in alist:
	print(item, end=" ")
print()
"""

for row in lists:
	for col in row:
		print(col, end=" ")
	print()