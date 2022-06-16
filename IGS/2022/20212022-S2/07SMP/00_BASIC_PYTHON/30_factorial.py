
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 4! = 4 x 3 x 2 x 1 = 24
num = 4
res = 1

def factorial(number):
	global res
	res *= number

while (num > 1):
	factorial(num)
	num -= 1

print(res)