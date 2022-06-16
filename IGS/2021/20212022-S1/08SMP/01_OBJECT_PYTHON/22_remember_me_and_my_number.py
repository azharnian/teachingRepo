from random import randint
import json

def greet_user():

	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}.")


def get_stored_username():
	filename = "22_username.json"
	try:
		with open(filename, 'r') as data: #r -> read
			username = json.load(data)
	except json.decoder.JSONDecodeError:
		return None			
	else:
		return username

def get_new_username():
	username = input("What is your name? ")
	with open("22_username.json", 'w') as data:
		json.dump(username, data)
	return username	

def ask_user():

	favorite_number = get_stored_number()
	if favorite_number:
		print(f"I know your favorite number! it's {favorite_number}")
	else:
		favorite_number = get_new_number()
		print(f"We'll remember your favorite number!")


def get_stored_number():

	filename = "22_favorite_number.json"
	try:
		with open(filename, 'r') as data:
			favorite_number = json.load(data)
	except json.decoder.JSONDecodeError:
		return None
	else:
		return favorite_number

def save_favorite_number(favorite_number):
	with open("22_favorite_number.json", "w") as data:
		json.dump(favorite_number, data)


def get_new_number():
	random_number = randint(1, 100)
	username = get_stored_username()
	guessing = input(f"I'll guess your favorite number is {random_number}, is it right {username} ? (y/n) ")
	if guessing.lower() == 'y':
		favorite_number = random_number
	else:
		favorite_number = input("hmm, so what is your favorite number ? ")
	save_favorite_number(favorite_number)
	return favorite_number


greet_user()
ask_user()


