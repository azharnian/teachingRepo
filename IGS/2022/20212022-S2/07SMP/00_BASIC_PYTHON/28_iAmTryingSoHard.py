
while True:
	a = input()
	b = input()

	# print(int(a)/int(b))
	try:
		#print(int(a)/int(b))
		result = int(a)/int(b)
	except ZeroDivisionError:
		print("OMG, please avoid 0 number as denominator!")
	except ValueError:
		print("Please input a number!")
	else:
		print(result)
	finally:
		print("done")

	quit = input("Want to Quit (y/n)? ")
	if quit.lower() == "y":
		break