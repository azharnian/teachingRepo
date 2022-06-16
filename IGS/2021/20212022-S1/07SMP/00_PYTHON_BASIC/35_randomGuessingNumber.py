import random

correct_number = random.randint(0,100)
guessing_number = None 
#print(correct_number)
while guessing_number != correct_number:
	guessing_number = int(input("Guess the number : "))

	if guessing_number == correct_number:
		print("Yeay Correct!")
	else:
		print("Incorrect!")
		if guessing_number > correct_number:
			print(f"correct number is less than {guessing_number}")
		else:
			print(f"correct number is more than {guessing_number}")
	"""
	if guessing_number == correct_number:
		print("Yeay Correct!")
	elif guessing_number > correct_number:
		print("Incorrect!")
		print(f"correct number is less than {guessing_number}")
	else:
		print("Incorrect!")
		print(f"correct number is more than {guessing_number}")
	"""
