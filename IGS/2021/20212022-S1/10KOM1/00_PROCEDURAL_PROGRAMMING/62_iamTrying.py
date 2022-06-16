#Try Except ... "Handling Error"

while True:
	a = input("a = ")
	b = input("b = ")

	try:
		print(f"a : b = {int(a)/int(b)}")
	except:
		print("You can't devide by zero.")
	quit = input("Quit (y/n)? ")
	if quit == "y":
		break