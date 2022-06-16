"""
4! 	= 	4 x 3!
	=	4 x (3 x 2!)
	=	4 x (3 x (2 x 1!))
	=	4 x (3 x (2 x (1 x 0!)))
	=	4 x (3 x (2 x (1 x 1)))
"""
def main():
	num = 10
	print(factorial(num))

def factorial(number):
	if number < 0:
		return # ekuivalen dengn return None
	if number == 0 or number == 1:
		return 1
	return number * factorial(number-1)

main()