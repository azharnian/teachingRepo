
play = True #flag - penanda - variable trigger

while play:
	print("we are playing now!")
	still_playing = input("Still Playing (Y/N) : ")
	if still_playing == "N":
		play = False