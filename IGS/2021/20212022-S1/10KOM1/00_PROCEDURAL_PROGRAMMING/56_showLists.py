# alist = [1, 2, 3, 4, 5]

alist = [
	[1, 2, 3, 4, 5], # [0][0] [0][1] [0][2]
	[6, 7, 8, 9, 10], # [1][0] 
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20] # ... [4][4]
]

"""
for item in alist:
	print(item, end=" ")
print()
"""

for row in alist:
	for col in row: #col -> column
		print(col, end=" ")
	print()
