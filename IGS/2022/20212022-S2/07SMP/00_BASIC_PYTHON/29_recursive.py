#This program made by Anas

num = 0

def counter(number):
	print(number)
	number += 1
	if number < 10: #recursive case
		counter(number)
	# else: #base case (stop looping)
	# 	return

# for i in range(10):
# 	counter(num)
# 	num += 1

# while ( num < 10):
# 	counter(num)
# 	num += 1

counter(num)