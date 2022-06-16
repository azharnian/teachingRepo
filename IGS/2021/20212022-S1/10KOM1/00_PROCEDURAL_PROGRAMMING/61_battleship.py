import random
import os

def setting_up_board(rows):
	board = []

	for row in range(rows):
		line = []
		for item in range(rows):
			line.append("O") # ["O", "O", "O", "O", "O"]
		board.append(line)
		"""	
		[
		["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ..
		]
		"""
	return board

def setting_up_ship_location(rows):
	location = [str(random.randint(0, rows-1)), str(random.randint(0, rows-1))] # [x, y]
	return location

def printing_board(board):
	os.system("clear") # windows : cls
	for row in board:
		for item in row:
			print(item, end=" ")
		print() #kalau sudah selesai satu baris

def check_user_input():
	user_input = input("Enter Ship Location: ").split(" ") # 2 2
	if my_ship == user_input:
		return True
	else:
		my_board[int(user_input[0])][int(user_input[1])] = "X" # my_board[row][col] > "O"  > " "
		return False


win = False
attempt = 1

my_board = setting_up_board(5)
my_ship = setting_up_ship_location(5)

while not win:
	printing_board(my_board)
	# print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1

print(f"Congratulation ..., you win, with {attempt} attempts.!")
	



