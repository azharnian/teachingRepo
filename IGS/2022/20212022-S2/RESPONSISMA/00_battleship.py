import os
import random

#string immutable
setting_up_board = lambda n : [ list("X" * n) for _ in range(n) ]

setting_up_ship_location = lambda rows : [random.randint(0, rows-1), random.randint(0, rows-1)]

def printing_board(board):
	os.system("clear") # windows : cls
	for row in board:
		print(" ".join(row))

def check_user_input():
	user_input = list(map(int, input("Enter the coordinate to launch our misile <x> <y> ").split()))

	if user_input == my_ship:
		print("Congrats! you win the game.")
		return True

	my_board[user_input[0]][user_input[1]] = "O"


	return False


win = False
rows = 5
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)

while not win:
	printing_board(my_board)
	# print(my_ship)
	win = check_user_input()

















