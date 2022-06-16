import os
os.system("clear") #untuk bersihkan console microsoft -> 'cls'
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")


while True: #infinnite loop
	first_number = input("\nFirst Number : ") #text '2'/'2' default data type (str)
	if first_number.lower() == 'q':
		break
	second_number =input("\nSecond Number : ")
	if second_number.lower() == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	#except Exception as error_msg:
		#print("You can't divide by zero!.")
		#print(error_msg)
	except ZeroDivisionError:
		print("You can't divide by zero!.")
	except ValueError as e:
		print(f"PYTHON_ERROR_MSG : {e}")
		print("Please input number!.")
	else:
		print(f"The answer is {answer}")
	finally:
		print("Done!")

	