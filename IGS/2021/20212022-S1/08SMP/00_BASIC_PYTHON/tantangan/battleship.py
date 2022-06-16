import os
import random
#board = [ "O", "O", "O", "O", "O", "O", "O", "O", "O"]
#          0    1    2    3    4    5    6    7    8
#What is Lists ? - Index(alamat) dan Value(data)
#board = { "blokA":"O", "blokB":"O"} # Key dan Value
board = [
	["O", "O", "O"],
	["O", "O", "O"],
	["O", "O", "O"]
] #Lists 2 Dimensions

# counter += 1

#ship = (0,1)
ship = (random.randint(0,2),random.randint(0,2)) # Tuple - (Lists yg ga bisa di remove, pop, del, append)

missile = (None, None)

play = True

while play:
	os.system('clear')
	for row in board:
		print(row)

	row_guess = int(input("Put Row Missile : ")) #0,1,2
	column_guess = int(input("Put Column Missile : ")) #0,1,2
	missile = (row_guess,  column_guess)
	if missile == ship:
		print("Boomzzz, gotchaa")
		play = False
	else:
		print("You are so lame ...")
		input("Enter to Try Again.")
		board[row_guess][column_guess] = "X"
