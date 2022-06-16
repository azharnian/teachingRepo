import random
import os


def intro():

	#remember_me nya di sini
	
	try:
		os.system("clear")
		print("Welcome To Battleship CMD Version 2021")
		result = int(input("Please input how many rows you wanna play: "))

		if result < 3 or result > 10:
			print("You must input a number more than 2 or less than or equal 10.")
			input("Enter to try again")
			return intro()

		return result

	except ValueError as e:
		print(f"You must input an integer number!\nPython Error:{e}")
		input("Enter to try again")
		return intro()


	return input("Pelase input how many rows you wanna play: ")

def setting_up_board(rows):
	board = []

	for row in range(rows):
		line = []
		for item in range(rows):
			line.append("O") # ["O", "O", "O", "O", "O"]
		board.append(line)
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
	try:
		user_input = input("Enter Ship Location: ").split(" ")
		if len(user_input) != 2:
			print("You must input 2 integer numbers!")
			input("Enter to Try Again")
			return check_user_input()
		user_input = [str(int(user_input[0])-1), str(int(user_input[1])-1)]
	except ValueError as e:
		print(f"You must input an integer number!\nPyErr:{e}")
		input("Enter to Try Again")
		return check_user_input()
	else:
		if int(user_input[0]) < 0 or int(user_input[0]) > rows-1 or int(user_input[1]) < 0 or int(user_input[1]) > rows-1:
			print(f"You must input number between 1 and {rows}")
			input("Enter to Try Again")
			return check_user_input()
		if my_ship == user_input:
			return True
		my_board[int(user_input[0])][int(user_input[1])] = "X" # my_board[row][col]
		return False


def congrats():
	print(f"Congratulation ..., you win, with {attempt} attempts.!")


win = False
attempt = 1

rows = intro()
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)

while not win:
	printing_board(my_board)
	# print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1

congrats()	



