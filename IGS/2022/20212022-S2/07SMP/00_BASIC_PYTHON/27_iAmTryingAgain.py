
while True:
	a = input()
	b = input()

	try:
		print(int(a)/int(b))
	except :
		print("OMG, please avoid 0 number as denominator!")

	quit = input("Want to Quit (y/n)? ")
	if quit.lower() == "y":
		break