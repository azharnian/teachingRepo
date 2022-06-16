import os

def setting_up_board():

	"""
	[
	["X", "O", "O", "O", "O"],
	["O", "O", "O", "O", "O"],
	["O", "O", "X", "O", "O"],
	["O", "O", "O", "O", "O"],
	["O", "O", "O", "O", "O"]
	]

	"""

	board = []

	for row in range(5):
		line = []
		for item in range(5):
			line.append("O")
		board.append(line)

	return board


def printing_board(board):
	os.system("clear")
	# print(my_board)
	for row in my_board:
		for item in row:
			print(item, end=" ")
		print()

def check_user_input():
	user_input = input("Enter ship location: ")


win = False
attempt = 1

my_board = setting_up_board()


while not win:
	printing_board(my_board)
	win = check_user_input()
	if not win:
		attempt += 1


