import os
import random
def setting_up_board():
	board =[]
	rows = 5
	for row in range(rows):
		line = "O" * rows # because string is immutable (the value cannot change)
		# print(line)
		board.append(list(line))
	return board


def printing_board(board):
	os.system("clear"); #cls for windows
	for row in board:
		# print(row[0], row[1], row[2], row[3], row[4])
		for item in row:
			print(item, end="\t")
		print("\n")

def setting_up_ship_location(rows):
	x = str(random.randint(0, rows-1))
	y = str(random.randint(0, rows-1))
	location = [x,y]
	return location

def check_user_input():
	user_input = input("Put the location to launch our misile <x> <y>: ").split(" ")

	if user_input == my_ship:
		print("You Win!")
		return True
	x = int(user_input[0])
	y = int(user_input[1])
	my_board[x][y] = "X" # "O" -> "X"


	return False 

win = False
my_board = setting_up_board()
my_ship = setting_up_ship_location(5)

while not win:
	printing_board(my_board)
	# print(my_ship)
	win = check_user_input()
	

