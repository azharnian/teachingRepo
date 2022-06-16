
"""
def isOdd(x):
	return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_a = []

for item in a:
	if isOdd(item):
		odd_a.append(item)


print(odd_a)
"""
def isOdd(x):
	return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#odd_a = list(filter(isOdd, a))
#odd_a = list(filter(lambda x: x%2 != 0, a))
odd_a = [ x for x in a if x%2 != 0 ]
print(odd_a)

