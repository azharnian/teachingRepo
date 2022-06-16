import json
import random

def load_data():
	try:
		with open("data.json", "r") as file:
			return json.load(file)
	except:
		return {} # {} != None	

def save_data(data):
	with open("data.json", "w") as file:
		json.dump(data, file)
		return True


def greet_user(data):
	# print(f"{hex(id(data))}, {type(data)}")
	username = input("What is your name ? ")
	if username in data:
		print(f"Welcome back {username}!")
	else:
		data[username] = None
		save_data(data)
		print("We'll remember you when you come back!")
	return username

def get_new_favorite_number(random_number):
	ans = input(f"I'll guess your favorite number is {random_number}, is it right ? (y/n)")
	if ans.lower() == "y":
		return random_number
	elif ans.lower() == "n":
		return int(input("So, what is your number ? "))
		#2 handling error kalau bukan integer number yg diinput.
	else:
		print("please answer with y or n.")
		return get_new_favorite_number(random_number)

def ask_user(data, user):
	if user in data:
		if data[user]:
			print(f"I know your favorite number, it is {data[user]}")
			#1 tawaran mau ubah favorite numbernya
		else:
			guess_number = random.randint(0, 100)
			favorite_number = get_new_favorite_number(guess_number)
			data[user] = favorite_number
			save_data(data)
			print(f"I'll remember your favorite number!")

data_master = load_data()
# print(f"{hex(id(data_master))}, {type(data_master)})")
ask_user(data_master, greet_user(data_master)) #pass by reference