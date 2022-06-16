m, n = input().split()
arr = []
for row in range(int(m)):
	numbers = input().split()
	arr.append(numbers)

for col in range(int(n)):
	for row in range(int(m)-1,-1,-1):
		print(int(arr[row][col]), end=" ")
	print()
