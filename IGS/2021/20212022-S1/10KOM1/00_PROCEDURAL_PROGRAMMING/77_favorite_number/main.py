import json
import random

def loading_data():
	with open("data.json", "r") as file:
		return json.load(file)

def saving_data():
	with open("data.json", "w") as file:
		json.dump(favorite_number, file)
		return True

def get_stored_number():
	try:
		return loading_data()
	except:
		return

def get_new_favorite_number(random_number):
	ans = input(f"I'll guess your favorite number is {random_number}, is it right ? (y/n)")
	if ans.lower() == "y":
		return guess_number
	elif ans.lower() == "n":
		return input("So, what is your number ? ")
	else:
		print("please answer with y or n.")
		return get_new_favorite_number(random_number)

def ask_user():
	favorite_number = get_stored_number()
	if favorite_number:
		print(f"I know your favorite number, it's {favorite_number}")
	else:
		guess_number = random.randint(0, 100)
		favorite_number = get_new_favorite_number(guess_number)
		saving_data()
		print(f"I'll remember your favorite number!")

ask_user()

