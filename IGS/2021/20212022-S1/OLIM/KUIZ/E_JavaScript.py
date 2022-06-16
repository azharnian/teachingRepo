numbers = input().split()
try:
	numbers = list(map(int, numbers))
	print(numbers[0]-numbers[1])
except:
	print("NaN")