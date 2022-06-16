
correct_number = 45
guessing_number = None 

while guessing_number != correct_number:
	guessing_number = int(input("Guess the number : "))

	if guessing_number == correct_number:
		print("Yeay Correct!")
	else:
		print("Incorrect!")