a_list = [
	[1, 2, 3, 4, 5], 		# [0][0] [0][1] [0][3] [0][4] [0][5]
	[6, 7, 8, 9, 10],		# [1][0] [1][1]
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20]
]

# for item in a_list:
# 	print(item, end=" ")
# print()

for row in a_list:
	for col in row:
		print(col, end=" ")
	print()