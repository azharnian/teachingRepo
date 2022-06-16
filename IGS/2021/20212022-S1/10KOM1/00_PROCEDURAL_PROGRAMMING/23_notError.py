
error = False #flag - penanda - variable trigger negasi

while not error:
	print("we are playing now!")
	still_playing = input("Still Playing (Y/N) : ")
	if still_playing == "N":
		error = True