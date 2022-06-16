"""
numbers = input().split(" ")
# a, b, c = int(a), int(b), int(c)
new_numbers = []

for number in numbers:
	new_numbers.append(int(number))


print(new_numbers)
"""

# def add_3(n):
# 	return n+3

#add_3 = lambda n : n+3

#numbers = list(map(int, input().split()))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#new_numbers = list(map(lambda n : n+3, numbers))
#new_numbers = [ add_3(x) for x in numbers ]
#print(new_numbers)

# buat list baru yg tiap item dikuadratkan dan diperoleh dari list numbers yang merupakan bilangan genap.

# [0, 4, 16, 36, 64] **

square = lambda x: x**2

new_numbers = [ square(number) for number in numbers if number%2 == 0 ]
print(new_numbers)




