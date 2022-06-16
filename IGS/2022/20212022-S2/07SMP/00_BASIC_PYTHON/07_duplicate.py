
numbers  = [7, 8, 5, 1, 3, 3, 5, 7]
numbers.sort()
# print(numbers)
curr = None
prev = None # Nothing!
for number in numbers:
	curr = number
	if curr == prev:
		print(curr)
	prev = curr