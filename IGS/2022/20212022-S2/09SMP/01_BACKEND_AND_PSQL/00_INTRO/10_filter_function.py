
# def isEven(x):
# 	return x%2==0

isEven = lambda x : x%2==0 # lambda function yg punya nama

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_a = list(filter(isEven, a))
# even_a = list(filter(lambda x: x%2==0, a)) #lambda anonymous (tidak punya/tidak dikenali)

# even_a = [ x for x in a if x%2==0 ]
even_a = [ number for number in a if number%2==0 ]

# for item in a:
# 	if isEven(item):
# 		even_a.append(item)


print(even_a)