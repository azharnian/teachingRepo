# Try Except .. ("Handling Error")

while True:
	a = int(input("a = "))
	b = int(input("b = "))
	try:
		print(f" a : b = {a/b}")
	except:
		print("You can't devide by zero!")
	quit = input("Quit ? (y/n) ")
	if quit == "y":
		break
